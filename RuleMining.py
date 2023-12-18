import csv

# This is an alternative way for DefaultDict library since defaultdict library is not allowed
def defaultdict(default_type):
    class DefaultDict(dict):
        def __getitem__(self, key):
            if key not in self:
                dict.__setitem__(self, key, default_type())
            return dict.__getitem__(self, key)
    return DefaultDict()
# This section of code is directly retrieved from stackoveerflow [1]

# Create the Apriori object
# Assign the access of the function to Apriori object
class Apriori(object):
    def __init__(self, min_sup, min_conf):
        self.min_sup = min_sup
        self.min_conf = min_conf
    # Initialization

    # Calculate the confidence
    def calculateConf(self, file_path):
        transactions = self.getTransactions(file_path)
        items = self.getItems(transactions)
        count = defaultdict(int)
        frequencies = dict()

        self.trans_length = len(transactions)
        self.items = items

        # Call the get item min_sup to build 1-termset
        current_frequency = self.getItemsMinSupport(transactions, items, count, self.min_sup)

        k = 1
        # Increment the k-value and repeat the while loop until the current frequency is an empty set
        while current_frequency != set():
            k += 1
            frequencies[k] = current_frequency
            upd_items = self.buildItemsSet(current_frequency, k)
            current_frequency = self.getItemsMinSupport(transactions, upd_items, count, self.min_sup)
        self.count = count
        self.frequencies = frequencies

        return count, frequencies

    # build item set
    def buildItemsSet(self, terms, k): 
        itemSet = set()
        for term1 in terms:
            for term2 in terms:
                if len(term1.union(term2)) == k:
                    itemSet.add(term1.union(term2))        
        return itemSet

    # get items from transaction
    def getItems(self, transactions):
        itemSet = set()
        for line in transactions:
            for item in line:
                itemSet.add(frozenset([item]))
        return itemSet

    # get the transaction pair list
    def getTransactions(self, file_path):
        transactions = []
        with open(file_path, 'r') as file:
            file = csv.reader(file, delimiter=',')
            for line in file:
                line_items = []
                for item in line:
                    line_items.append(item)
                transactions.append(line_items)

        headers_set = transactions[0]
        transactions = transactions[1:]
        transactions_pair = []
        for transaction in transactions:
            element = set([(header, item) for header, item in zip(headers_set, transaction)])
            # nested for loop in one line [2]
            transactions_pair.append(element)
        return transactions_pair

    # get the item support set
    def getItemsMinSupport(self, transactions, items, frequencies, min_sup):
        itemSupport = set()
        local_set_ = defaultdict(int)
        for item in items:
            for trans in transactions:
                if item.issubset(trans):
                    frequencies[item] += sum([1])
            for trans in transactions:
                if item.issubset(trans):
                    local_set_[item] += sum([1])
        #  double nested for loop
        n = len(transactions)
        for item, cnt in local_set_.items():
            if float(cnt)/n >= min_sup:
                itemSupport.add(item)  

        return itemSupport

    # generate association rules
    def getRules(self, rhs):
        rules = dict()
        for key, value in self.frequencies.items():
            for item in value:
                if rhs.issubset(item) and len(item) > 1:
                    itemSupport = self.getSupport(item)
                    item = item.difference(rhs)
                    conf = itemSupport / self.getSupport(item)
                    if conf >= self.min_conf:
                        rules[item] = (itemSupport, conf)
        return rules

    # get the support value
    def getSupport(self, item):
        return self.count[item] / self.trans_length

def main():
    input_file_path = "Play_Tennis_Data_Set.csv"
    output_file_path = "Rules.txt"
    min_sup = float(input("\nEnter the number for support(min_sup): "))
    min_conf = float(input("\nEnter the number for confidence(min_conf): "))

    # call the object
    apriori = Apriori(min_sup, min_conf)
    # access the object
    count, frequencies = apriori.calculateConf(input_file_path)
    
    # print out the value with the required format in the txt file
    file_out = open(output_file_path, "w")
    file_out.write("User Input\n\nSupport={}\nConfidence={}\n\n".
                   format(min_sup, min_conf))
    file_out.write("Rules:\n")

    index = 1
    for item in apriori.items:
        rules = apriori.getRules(item)
        for key, value in rules.items():
            key_list = list(key)[0]
            item_list = list(item)[0]
            file_out.write("Rule#{}: {{{}={}}} => {{{}={}}}".format(index, key_list[0], key_list[1], item_list[0], item_list[1]))
            file_out.write("\n(Support=%.2f, Confidence=%.2f)\n\n" % (value[0], value[1]))
            index += 1

if __name__ == '__main__':
    main()

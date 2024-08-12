import pandas as pd
sales_file = 'sales.csv'
inventory_file = 'inventory.csv'
customers_file = 'customers.csv'
products_file = 'products.csv'
stores_file = 'stores.csv'

def load_data():
    sales = pd.read_csv(sales_file)
    inventory = pd.read_csv(inventory_file)
    customers = pd.read_csv(customers_file)
    products = pd.read_csv(products_file)
    stores = pd.read_csv(stores_file)
    return sales, inventory, customers, products, stores

def clean_data(sales, inventory, customers, products, stores):
    sales.drop_duplicates(inplace=True)
    inventory.drop_duplicates(inplace=True)
    customers.drop_duplicates(inplace=True)
    products.drop_duplicates(inplace=True)
    stores.drop_duplicates(inplace=True)
    sales.fillna(0, inplace=True)
    inventory.fillna(0, inplace=True)
    customers.fillna('', inplace=True)
    products.fillna('', inplace=True)
    stores.fillna('', inplace=True)
    sales['SaleDate'] = pd.to_datetime(sales['SaleDate'])
    
    return sales, inventory, customers, products, stores

def combine_data(sales, inventory, customers, products, stores):
    sales_details = pd.merge(sales, products, on='ProductID', how='left')
    sales_details = pd.merge(sales_details, customers, on='CustomerID', how='left')
    sales_details = pd.merge(sales_details, stores, on='StoreID', how='left')
    return sales_details

def analyze_data(sales_details, inventory):
    inventory_status = inventory.groupby('ProductID').agg({
        'StockLevel': 'sum',
        'ReorderPoint': 'mean'
    })
    sales_trends = sales_details.groupby(sales_details['SaleDate'].dt.to_period('M')).agg({
        'Quantity': 'sum',
        'Revenue': 'sum'
    })
    
    return inventory_status, sales_trends

def main():
    sales, inventory, customers, products, stores = load_data()
    sales, inventory, customers, products, stores = clean_data(sales, inventory, customers, products, stores)
    sales_details = combine_data(sales, inventory, customers, products, stores)
    inventory_status, sales_trends = analyze_data(sales_details, inventory)
    print("\nInventory Status:")
    print(inventory_status.head())
    
    print("\nSales Trends:")
    print(sales_trends.head())

if __name__ == '__main__':
    main()

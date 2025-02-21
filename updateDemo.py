import pandas as pd
import os

data = pd.read_excel("data/newDemoData.xlsx")

# data.head()

customerName = data["Customer Name"].unique()
# productGroup = data["Product group"].unique()
# product = data["Product"].unique()
print(customerName)
# print(len(productGroup))
# print(len(product))


newGroup = ["Bespoke Furniture",
"Commercial Fit-outs",
"Architectural Joinery"]

oldGroup = ["Cuts and Portions",
"Other Products",
"Whole Ducks"]

groupDict = dict(zip(oldGroup,newGroup))

groupDict.values()

newProducts = ["Bespoke Kitchen Cabinetry",
"Fitted Wardrobes",
"Bespoke Office Furniture",
"Custom Shelving Units",
"Built-in Bookcases",
"Reception Counters",
"Hardwood Internal Doors",
"Custom Staircases",
"Wooden Window Frames",
"Architectural Wood Panelling"]

oldProduct =["Duck Fillets 250g",
"Duck Breast Portions 400g",
"Duck Legs 500g Pack",
"Boneless Duck Thighs 300g",
"Duck Wings 600g Pack",
"Roasting Duck - Premium Grade (2.2kg)",
"Whole Duck - Small (1.5kg)",
"Whole Duck - Medium (2kg)",
"Whole Duck - Large (2.5kg)",
"Marinated Duck Fillets 300g"]



newCustomers = ["Horizon Architects Ltd.",
"Studio Elemental Design",
"Vertex Engineering Group",
"Summit Interiors",
"Blueprint QS Services",
"Forma Design Consultants",
"Axis Space Architects",
"Echelon Design & Build"]

customerDict = dict(zip(customerName, newCustomers))

productDict = dict(zip(oldProduct,newProducts))

data.head()
data["Product group"] = data["Product group"].replace(groupDict)
data["Product"] = data["Product"].replace(productDict)
data["Customer Name"] = data["Customer Name"].replace(customerDict)

data["Company"].unique()

data.to_excel("newDemoData.xlsx")


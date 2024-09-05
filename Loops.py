# List -> Store multiple values of different types
list_of_cloud = ["AWS", "Azure","GCP", "Oracle Cloud", "AliBaba Cloud"]
print(list_of_cloud)

# Add new element to the list at the end 
list_of_cloud.append("Samsung Cloud")
list_of_cloud.append("IBM Cloud")
print(list_of_cloud)

#Insert Element at a position (starts from '0' index)
list_of_cloud.insert(4,"Salesforce Cloud")
print(list_of_cloud)

#To find the length of the list
print("Lenght Of List:",len(list_of_cloud))

#To Iterate the elements in list_of_cloud
for i in list_of_cloud:
    print("\t",i)

#To iterate using For Loop
for j in range(0,3):
    print(j)

#To iterate using While loop
a=0
while a in range(0,5):
    print(a)
    a+=1
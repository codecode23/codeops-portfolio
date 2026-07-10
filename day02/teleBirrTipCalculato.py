total=1000
people=[
"john","sara","abebe"
]

def split_bill(total, people, tip_rate=0.10):
    tip=total*tip_rate
    new_total=tip+total
    per_person=new_total/(len(people))
    return per_person
for each_name in people:
    print(f"{each_name} should pay: {split_bill(total, people)}")

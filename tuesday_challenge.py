#!/usr/bin/python3

mess = {"all":[{"First":"Corey","Last":"Hollins","Skill Level":"G.O.A.T.","Spirit Animal":"zebra","Super Power":"Mind control"},{"First":"David","Last":"Benjamin","Skill Level":"astonishing","Spirit Animal":"seal","Super Power":"Technopathy"},{"First":"Greg","Last":"Green","Skill Level":"awe-inspiring","Spirit Animal":"barracuda","Super Power":"Prehensile\/animated hair"},{"First":"Jack","Last":"Stephens","Skill Level":"stunning","Spirit Animal":"ram","Super Power":"Levitation"},{"First":"James","Last":"Peterson","Skill Level":"wondrous","Spirit Animal":"otter","Super Power":"Psychic"},{"First":"Jamie","Last":"Vinciguerra","Skill Level":"breathtaking","Spirit Animal":"lion","Super Power":"Portal creation"},{"First":"Jordan","Last":"Campbell","Skill Level":"wonderful","Spirit Animal":"badger","Super Power":"Immortal"},{"First":"Josh","Last":"Bartels","Skill Level":"fearsome","Spirit Animal":"boar","Super Power":"Super speed"},{"First":"Kyle","Last":"Kander","Skill Level":"formidable","Spirit Animal":"goat","Super Power":"Elasticity"},{"First":"Rasheen","Last":"Kirkland","Skill Level":"frightening","Spirit Animal":"shark","Super Power":"Force fields"},{"First":"Brett","Last":"Ezell","Skill Level":"shocking","Spirit Animal":"penguin","Super Power":"Resurrection"},{"First":"Thomas","Last":"Stratton","Skill Level":"overwhelming","Spirit Animal":"tiger","Super Power":"Sonic scream"},{"First":"Tim","Last":"O'Fallon","Skill Level":"magnificent","Spirit Animal":"bison","Super Power":"Invisibility"},{"First":"Tristan","Last":"Lindquist","Skill Level":"impressive","Spirit Animal":"hornet","Super Power":"Freezing breath"},{"First":"Yun","Last":"Chang","Skill Level":"intimidating","Spirit Animal":"fox","Super Power":"Animal control"}]}

#print('My name is', mess["all"][9]["First"], 'and my spirit animal is', mess["all"][9]["Spirit Animal"])

#print('My name is', mess["all"][9]["First"], 'and my skills level is', mess["all"][9]["Skill Level"])

#print('My name is', mess["all"][9]["First"], 'and my super power is', mess["all"][9]["Super Power"])

def main():
    list = mess["all"]
    for x in list:
        print(f"Name: {x['First']}")
        print(f"Skill Level: {x['Skill Level']}")
        print(f"Spirit Animal: {x['Spirit Animal']}")
        print(f"Super Power: {x['Super Power']}\n")

main()

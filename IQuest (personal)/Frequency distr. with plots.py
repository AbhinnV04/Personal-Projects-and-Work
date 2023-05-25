"""
# DEV NOTES:
* You wont go collecting data individually through a single script. You would need a web-app or something to work as a universal counter or something, Ideally you would do a google form survey or something that will give you a spreadsheet or csv etc, And you would need a script to read that
* I dont have experience with spreadsheet scripts yet, I am working on it, so this is a proof of concept with a txt file
* I used chatgpt to create a list a people and their preferred time slots between 7 and 11:30 to create a random dataset because, yeah thats when a meeting would be really
* Also, I am learning Data Science so this format seemed the most relevant for me.
"""

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Matplotlib'])
    

RESPONSES= []
TEMP = []
FREQ = {}

def createRandomResponse():
    with open('resp.txt', 'w+') as file:
        file.write("Emma: 7:30pm\nLiam: 9:00pm\nOlivia: 10:15pm\nNoah: 7:45pm\nAva: 7:30pm\nIsabella: 9:30pm\nSophia: 10:00pm\nMia: 7:30pm\nJackson: 8:45pm\nAiden: 9:00pm\nLucas: 10:15pm\nHarper: 7:30pm\nEthan: 8:15pm\nAmelia: 9:45pm\nEvelyn: 10:30pm\nAbigail: 7:15pm\nAlexander: 9:15pm\nCharlotte: 10:00pm\nEmily: 8:15pm\nJames: 9:30pm\nBenjamin: 7:30pm\nDaniel: 8:45pm\nHenry: 10:15pm\nMatthew: 7:30pm\nHarper: 8:30pm\nSamuel: 9:45pm\nMichael: 10:30pm\nAmelia: 7:15pm\nOliver: 8:30pm\nElijah: 9:45pm\nEthan: 10:30pm\nEvelyn: 7:30pm\nAlexander: 8:45pm\nDaniel: 10:00pm\nGrace: 10:15pm\nNoah: 7:15pm\nAva: 8:30pm\nEmily: 9:45pm\nWilliam: 10:30pm\nMia: 7:15pm\nHarper: 8:30pm\nOliver: 9:45pm\nLiam: 10:30pm\nBenjamin: 7:15pm\nSamuel: 8:30pm\nEvelyn: 9:45pm\nHenry: 10:30pm\nJames: 7:15pm\nEmma: 8:30pm\nDaniel: 9:45pm")
        # assumption made that 15 min slots are taken between 7pm to 11:30pm, since this depends on the dataset


def readResponse(loc = "resp.txt"):
    with open(loc) as my_file:
        for line in my_file:
            TEMP = line.split(" ")
            RESPONSES.append(TEMP[1])

	
def frequency():
    for i in RESPONSES:
        if i in FREQ:
            FREQ[i] += 1
        else:
            FREQ[i] = 1


def plot():
    plt.bar(FREQ.keys(), FREQ.values(), 1)
    plt.title("Time slot selection response")
    plt.xlabel("Time slots")
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()


def main():
    createRandomResponse()
    #location = input("Enter the file path: ")                  # /For a custom location of the file./
    readResponse()
    #print(RESPONSES)
    frequency()
    #print(FREQ)
    print(max(FREQ))
    plot()
    
    
if __name__ == '__main__':
    main()
            
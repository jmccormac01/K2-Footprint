from datetime import datetime
import json
import matplotlib.pyplot as plt

fp = json.load(open('K2_fields.json'))
fpn = json.load(open('K2_fields_new.json'))

# current campaign
for campaign in fp.keys():
    start = datetime.strptime(fp[campaign]['start'],'%Y-%m-%d')
    end = datetime.strptime(fp[campaign]['stop'],'%Y-%m-%d')
    now = datetime.utcnow()

    if now < start:
        colour = 'black'
    elif now > end:
        colour = 'red'
    else:
        colour = 'green'
    for channel in fp[campaign]['channels']:
        myChannel = fp[campaign]['channels'][channel]
        plt.plot(myChannel['corners_ra'] + myChannel['corners_ra'][:1],
                 myChannel['corners_dec'] + myChannel['corners_dec'][:1], color=colour)

# newly proposed campaigns
for campaignn in fpn.keys():
    colour = 'blue'
    for channeln in fpn[campaignn]['channels']:
        myChanneln = fpn[campaignn]['channels'][channeln]
        plt.plot(myChanneln['corners_ra'] + myChanneln['corners_ra'][:1],
                 myChanneln['corners_dec'] + myChanneln['corners_dec'][:1], color=colour)

plt.title('K2 Footprint')
plt.xlabel('Right Ascension')
plt.ylabel('Declination')
plt.ylim(-90, 50)
plt.xlim(0,360)
plt.savefig('K2Footprint.png',dpi=200)


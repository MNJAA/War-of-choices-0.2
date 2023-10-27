# This is the STORIES file
# why in another file because I think it's more orginaized. 
# and it will be imported to main.py

# An escape code (ANSI) to make space between lines instead of using \n
from ANSI import SL, Y, un

stories_list = [f"Betrayed at dawn:Your quest for vengeance","story 2(soon)","story 3(soon)"] 

def stories_listing():
	for number, story in enumerate(stories_list, start=1):
		print(f"{Y}{number}- {story}{SL}{un}")

# story one starting 
story_1 = {"chapters": {"intro": f"{SL}In the blazing Anbar desert,{SL} Sultan and his loyal unit, under Captain Amir's leadership,{SL} share unbreakable bonds. However,{SL} a lurking storm of secrets and betrayals challenges their unity.{SL * 2} You're going to play as 'Sultan' {SL}",
	
	"chapter1": f"{SL}The Desert Bond {SL} You're a 25-year-old soldier, stationed in the sweltering Anbar desert of Iraq.{SL} The unbreakable camaraderie within your unit is your source of strength.{SL} The bond you share with your unit members, forged through hardships,{SL} is a testament to your trust in Captain Amir, your leader. The night sky is soon pierced by a fierce,{SL} whipping wind that sends desert sands into a frenzy. Emerging from this tempest are General Rashid and his enigmatic forces,{SL} General Rashid's eyes mystery, reflect hidden truths as he orders your unit to surrender.{SL} Your heart sinks as you observe Captain Amir, your trusted leader,{SL} conferring closely with the general, and you know he wouldn't act without reason.",
	
	"chapter2": f"{SL}Captain Amir nodded at your suggestion to surrender.{SL} The unit members placed their weapons{SL} on the desert sand. As the sun set{SL} on the Anbar desert, the unit followed {SL}General Rashid's forces into the unknown, still{SL} wary of the unfolding events.{SL} In the days to come, you would{SL} discover that your choice had sealed your fate.{SL} General Rashid's true intentions remained{SL} shrouded in mystery, and the desert's{SL} secrets would challenge your resolve as you {SL}strove to survive and protect your unit."
	}

#story choices that will be shoed to the user and will determine what should be printed next
	"choices": {
		"chapter1c":{"surround": f"Captain, maybe we should consider surrendering, there might be a chance for peace and our safety.",

					"fight": f"Captain, I say we fight back, We can't afford to be caught off guard."
		},

	}
}
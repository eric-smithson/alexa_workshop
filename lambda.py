from __future__ import print_function
import json
import random

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))
    
    session_attributes = {}
    intent_info = event["request"]["intent"]
    if intent_info["name"] == "GetNewRapIntent":
        output = get_random_rap()
    elif intent_info["name"] == "GetRapFromArtistIntent":
        output = get_specific_rap(intent_info["slots"]["Artist"]["name"])
    else:
        output = get_random_rap()

    title = "Lil Botty"
    should_end_session = True
    reprompt_text = ""

    return build_response(session_attributes, build_speechlet_response(title, output, reprompt_text, should_end_session))

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    speechoutput = output #"<speak>" + output + "</speak>"
    return {
        "outputSpeech": {
            "type": "SSML",
            "ssml": speechoutput
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": ""
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }

def get_specific_rap(rap_artist):
    rap_dict = {}
    rap_dict["snoop"] = "<speak>Snoop Dogg. Man you got me goin crazy baby. Feel like I'm losin my mind. Throw your set up and wave it from Rolling side to c side. I'm talking big shit holdin my bitch. Banging on you cuz nigga this crip. Izzle kizzle fo' schizzle. My nizzle what you sizzle?. Fo' schizzle bizzle ha ha. That Snoop is back in dis mothafucka handlin' his biz. Takin' care of his kids and makin' hits, oh shiz. </speak>"
    rap_dict["kanye"] = "<speak>We got brothers full of Arm'i mami's in Manolo. Bags by Chanel all Louis Vuitton logos. All attracted to Hov' because they know dough. But at least it got girls callin' me 'Babycakes'. Now maybe Kay can hit 'em or Nas with Lazy K. And lady may maybe hey. Ladies and gentlemen let's put our hands together for the astonishing. H to the izz O V to the izz A. And I know that Linda was a hip hop head. And I know that Linda gave Hip Hop head. But I feel I could convert her. Cuz I ain't here to hurt her mayn. And I could rap to the beat but I don't know how to change my wage. I still hear a pull and I track 'em and strack 'em and whack 'em. Jack a nigga for the day to days and I yak 'em attack 'em and sack 'em. We deceive and we lie. And we keepin' it fly yo yo yo yo yo. Keeper of the skies. Baby It's me... Maybe I bore you. No No it's my fault cause I can't afford you. Maybe baby Puffy Jay Z. Could all be better for you. You rappers think I give a fuck about the way that they spit. Wanna be on my album but don't want me on they shit. Everybody thought I was makin' a compilation. I called her back from an earlier beep. Fo' in the mornin' they be like Nah I wasn't sleep. Convenient whore stay on top of convenient stores. Last week I paid a visit to the institute. They got the dropout keepin kids in the school. I guess I cleaned up my act like Prince'll do. If not for the pledge at least for the principal. They got the CD then got to see me. And I don't front and I don't go backwards. And I don't practice and I don't lack shit.</speak>"
    # rap_dict["50_cent"] = ""
    # rap_dict["eminum"] = ""
    # rap_dict[""]
    
    if rap_artist == "snoop" or rap_artist == "snoop dog":
        return rap_dict["snoop"]
    elif rap_artist == "kanye" or rap_artist == "kanye west" or rap_artist == "west":
        return rap_dict["kanye"]

    return rap_dict["kanye"]
    
def get_random_rap():
    rap_array = []
    #vulgar    
    rap_array.append("<speak>Cause they think that I'm a mother effin Beastie Boy, wolf whistle<break time=\".1s\"/> cause the way a hitta hatin' or trick plottin', the shit's hysterical<break time=\".3s\"/>No-no-i'm-not-sayin-i'm-the-best<break time=\".1s\"/> I'm just sayin<break time=\".1s\"/> I'm effin incredible! <break time=\".3s\"/>You took me to Australia. You put me on the fuckin' Paid Dues Festival.<break time=\".1s\"/>What you need for me, to flip that ish. and rip that ish?<break time=\".1s\"/>Or suck a stick and lick a stick. eat a stick<break time=\".1s\"/>Eat a mother effin' stick Chew on a prick and lick  <break time=\".1s\"/> A straight killer, a fool, a lil' ass gee<break time=\".1s\"/>Tell that mother effer to bring me some mother effin' weed, for this hospital<break time=\".1s\"/>Bitch read my mothereffin' chronicle<break time=\".1s\"/>My bitch boss Cristal<break time=\".1s\"/>Hit em high, hella height, historical.  <break time=\".5s\"/> I ain't never mother effin' stoppin' up in this mother effer<break time=\".1s\"/>Trick please you know how we do the undercover<break time=\".1s\"/>I'm obligated to study your moves then crush you mother fuckers<break time=\".1s\"/></speak>")
    # dope
    rap_array.append("<speak>Your money right but your credit aint then the bank still won't loan it. Your life's in a toilet, shit, get it on homie. Just holler at them boys because they keep plenty, follow me! Who the eff you think you is? Ron O'Neil.<break time=\".3s\"/>  Ok, here go the rundown, hittas gonna run down tell you put ya gun down. Cause it's not really a drought them other hittas just out. What you expect? 'Chall hittas want? I don't give a fuck now. cuz your daughter's known for givin' up the nappy dugout. <break time=\".3s\"/> This trick ain't saying ish cause the trick ain't ish. Dis is history in the making so shut the eff up and let me make it. I'm also down with La Face cuz L.A. Reid, yeah he pays me. Nah, I'm weezy effin effin effin effin baby. </speak>")    
    # emotional
    rap_array.append("<speak>Plus he had to be at home a long time ago. I used to be a player, I used to be afraid of being alone. To him I may just be another bro with a flow. Up in his torso, he ain't a boss so he can go.<break time=\".5s\"/>  Cause, ain't no possible way he can ever be true. And a long beard, I mean look, he look scary to me too. Well obviously oblivious to me I swore I was just invisible to you,  til I went to the lengths I did to meet you.  But that's fly by night for you, and the sky I write. If I was hit, and I was hurt, would you be by my side? I ain't proud of what I did amp if I could go back in time time. Ma roll up this back wood sweet pour a lil' Remy I.  And I look like I might just give up, eh you might've mistook. Stand up, and tell BAby you ain't gonna be shook. Man be yourself man you come around my crib you get your shit took. And you can achieve anything that you put your heart into. </speak>")

    random.seed()
    return rap_array[random.randrange(0, rap_array.__len__())]
    

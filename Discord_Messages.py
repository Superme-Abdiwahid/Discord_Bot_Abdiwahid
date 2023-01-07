import discord
import asyncio

intents = discord.Intents.all()
import json

client = discord.Client(intents=intents)
Token = ""
with open('token.json') as json_file:
    data = json.load(json_file)
    Token = data["token"]
@client.event
async def on_ready():
    print("Bot is online is ready to roll")
BADWORDS = ["4r5e", "5h1t", "5hit", "a55", "anal", "anus", "ar5e", "arrse", "arse", "ass", "ass-fucker", "asses",
            "assfucker", "assfukka",
            "asshole", "assholes", "asswhole", "a_s_s", "b!tch", "b00bs", "b17ch", "b1tch", "ballbag", "balls",
            "ballsack", "bastard",
            "beastial", "beastiality", "bellend", "bestial", "bestiality", "bi+ch", "biatch", "bitch", "bitcher",
            "bitchers", "bitches",
            "bitchin", "bitching", "bloody", "blow job", "blowjob", "blowjobs", "boiolas", "bollock", "bollok", "boner",
            "boob", "boobs", "booobs", "boooobs", "booooobs", "booooooobs", "breasts", "buceta", "bugger", "bum",
            "bunny fucker",
            "butt", "butthole", "buttmuch", "buttplug", "c0ck", "c0cksucker", "carpet muncher", "cawk", "chink", "cipa",
            "cl1t",
            "clit", "clitoris", "clits", "cnut", "cock", "cock-sucker", "cockface", "cockhead", "cockmunch",
            "cockmuncher",
            "cocks", "cocksuck", "cocksucked", "cocksucker", "cocksucking", "cocksucks", "cocksuka", "cocksukka", "cok",
            "cokmuncher", "coksucka", "coon", "cox", "crap", "cum", "cummer", "cumming", "cums", "cumshot",
            "cunilingus",
            "cunillingus", "cunnilingus", "cunt", "cuntlick", "cuntlicker", "cuntlicking", "cunts", "cyalis",
            "cyberfuc", "cyberfuck",
            "cyberfucked", "cyberfucker", "cyberfuckers", "cyberfucking", "d1ck", "damn", "dick", "dickhead", "dildo",
            "dildos", "dink",
            "dinks", "dirsa", "dlck", "dog-fucker", "doggin", "dogging", "donkeyribber", "doosh", "duche", "dyke",
            "ejaculate",
            "ejaculated", "ejaculates", "ejaculating", "ejaculatings", "ejaculation", "ejakulate", "f u c k",
            "f u c k e r", "f4nny",
            "fag", "fagging", "faggitt", "faggot", "faggs", "fagot", "fagots", "fags", "fanny", "fannyflaps",
            "fannyfucker",
            "fanyy", "fatass", "fcuk", "fcuker", "fcuking", "feck", "fecker", "felching", "fellate", "fellatio",
            "fingerfuck",
            "fingerfucked", "fingerfucker", "fingerfuckers", "fingerfucking", "fingerfucks", "fistfuck", "fistfucked",
            "fistfucker",
            "fistfuckers", "fistfucking", "fistfuckings", "fistfucks", "flange", "fook", "fooker", "fuck", "fucka",
            "fucked", "fucker",
            "fuckers", "fuckhead", "fuckheads", "fuckin", "fucking", "fuckings", "fuckingshitmotherfucker", "fuckme",
            "fucks", "fuckwhit",
            "fuckwit", "fudge packer", "fudgepacker", "fuk", "fuker", "fukker", "fukkin", "fuks", "fukwhit", "fukwit",
            "fux", "fux0r", "f_u_c_k",
            "gangbang", "gangbanged", "gangbangs", "gaylord", "gaysex", "goatse", "God", "god-dam", "god-damned",
            "goddamn", "goddamned",
            "hardcoresex", "hell", "heshe", "hoar", "hoare", "hoer",
            "homo", "hore", "horniest", "horny", "hotsex", "jack-off", "jackoff", "jap", "jerk-off", "jism", "jiz",
            "jizm", "jizz", "kawk",
            "knob", "knobead", "knobed", "knobend", "knobhead", "knobjocky", "knobjokey", "kock", "kondum", "kondums",
            "kum", "kummer", "kumming",
            "kums", "kunilingus", "l3i+ch", "l3itch", "labia", "lust", "lusting", "m0f0", "m0fo", "m45terbate",
            "ma5terb8", "ma5terbate",
            "masochist", "master-bate", "masterb8",
            "masterbat*", "masterbat3", "masterbate", "masterbation", "masterbations", "masturbate", "mo-fo", "mof0",
            "mofo", "mothafuck", "mothafucka",
            "mothafuckas", "mothafuckaz", "mothafucked", "mothafucker", "mothafuckers", "mothafuckin", "mothafucking",
            "mothafuckings", "mothafucks",
            "mother fucker", "motherfuck", "motherfucked", "motherfucker", "motherfuckers", "motherfuckin",
            "motherfucking", "motherfuckings",
            "motherfuckka", "motherfucks", "muff", "mutha", "muthafecker", "muthafuckker", "muther", "mutherfucker",
            "n1gga", "n1gger", "nazi",
            "nigg3r", "nigg4h", "nigga", "niggah", "niggas", "niggaz", "nigger", "niggers", "nob", "nob jokey",
            "nobhead",
            "nobjocky", "nobjokey", "numbnuts", "nutsack", "orgasim", "orgasims",
            "orgasm", "orgasms", "p0rn", "pawn", "pecker", "penis", "penisfucker", "phonesex", "phuck", "phuk",
            "phuked", "phuking", "phukked",
            "phukking", "phuks", "phuq", "pigfucker", "pimpis", "piss", "pissed", "pisser", "pissers", "pisses",
            "pissflaps", "pissin", "pissing",
            "pissoff", "poop", "porn", "porno", "pornography", "pornos", "prick", "pricks", "pron", "pube", "pusse",
            "pussi", "pussies", "pussy",
            "pussys", "rectum", "retard", "rimjaw", "rimming", "s hit", "s.o.b.", "sadist", "schlong", "screwing",
            "scroat", "scrote", "scrotum",
            "semen", "sex", "sh!+", "sh!t", "sh1t", "shag", "shagger", "shaggin", "shagging", "shemale", "shi+", "shit",
            "shitdick", "shite", "shited",
            "shitey", "shitfuck", "shitfull", "shithead", "shiting", "shitings", "shits", "shitted", "shitter",
            "shitters", "shitting", "shittings",
            "shitty", "skank", "slut", "sluts", "smegma", "smut", "snatch", "son-of-a-bitch", "spac", "spunk",
            "s_h_i_t", "t1tt1e5", "t1tties",
            "teets", "teez", "testical", "testicle", "tit", "titfuck", "tits", "titt", "tittie5", "tittiefucker",
            "titties", "tittyfuck",
            "tittywank", "titwank", "tosser", "turd", "tw4t", "twat", "twathead", "twatty", "twunt", "twunter",
            "v14gra", "v1gra", "vagina",
            "viagra", "vulva", "w00se", "wang", "wank", "wanker", "wanky", "whoar", "whore", "willies", "willy",
            "xrated", "xxx"]


@client.event
async def on_message(message):
    author_id = message.author.id
    if message.author.id == client.user.id:
        return;
    Split = str(message.content).split(" ")
    if message.author.id != client.user.id:
        for i in Split:
            index = findBadWord(i)
        if message.guild:
            if message.mentions:
                USERS_MENTIONED = [user.name for user in message.mentions]
                for users in USERS_MENTIONED:
                    print("Supreme")
                    if users == client.user.name:
                        for mention in message.mentions:
                            content = message.content.replace(mention.mention, '')
                            print(content.strip())
                        if content.lower() == "who is your boss":
                            await message.channel.send("My boss is Abdiwahid Bishar Hajir")
                            return
                        else:
                            print("Abdiwahid")
                            await message.channel.send("Yes How can I help you")
                            return
            if index >= 0 and not message.author.guild_permissions.administrator:
                await message.channel.send(message.author.mention +
                                           " PLEASE DO NOT USE FOUL LANGUAGE! DELETE THIS MESSAGE YOU JUST SENT! OTHERWISE YOU WILL BE "
                                           "KICKED FROM THIS SERVER / BANNED")
                return
            elif index >= 0 and message.author.guild_permissions.administrator:
                await message.channel.send(message.author.mention + " Calm Down avoid cursing, as an admin")
                return
            elif i.lower() == "help" and not message.author.guild_permissions.administrator:
                admins = []
                for member in message.guild.members:
                    if member.guild_permissions.administrator and not member.bot:
                        admins.append(member.mention)
                if admins:
                    await message.channel.send(f'{", ".join(admins)}')
                else:
                    await message.channel.send('Nobody is avaible to help')
                return
            elif i.lower() == "shutup":
                await message.channel.send(message.author.mention + " Thats not nice to say")
                return
            elif message.content.lower() == "my code is not working" and message.author.id != client.user.id:
                await message.channel.send("Please Be specific what is not working, so Abdi Can help")
                return
            elif not message.author.guild_permissions.administrator and message.content.isupper():
                await message.channel.send("Stop screaming! " + message.author.mention)
                return
            elif message.content.lower() == "*abdi":
                await message.channel.send("Abdiwahid " + "💯 💯 💯 🔥 🔥 🔥")
                return
            elif message.content.lower() == "*alive":
                await message.channel.send("I am Alive and Cooking")
                return
            elif message.content.lower() == "%bb":
                await message.channel.send("I am ready like always!")
                return;
            elif message.content.lower() == "dx":
                await message.channel.send("My plus is C is attached to me")
                return;
        else:
                print("Message author = ", message.author, "MEssage = ", message.content)
                await message.channel.send("I am Alive and Cooking")
                return
        # elif message.author.guild_permissions.administrator:
        #     await message.channel.send("Your an admin do whatever you want")
        #     return
        # elif not message.author.guild_permissions.administrator:
        #     await message.channel.send("Your not an admin")
        #     return

    if message.author.bot:
        return


def findBadWord(BAD_WORD):
    for i in range(0, len(BADWORDS)):
        if (BADWORDS[i] == BAD_WORD.lower()):
            return i;
    return -1;


client.run(Token)

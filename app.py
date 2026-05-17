import streamlit as st
import random

# --- PAGE CONFIG (Optimized for Mobile) ---
st.set_page_config(
    page_title="Manja Survival Kit",
    page_icon="🎀",
    layout="centered"
)

# Cozy, soft pink palette tailored for her phone
st.markdown("""
    <style>
    /* --- THIS FORCES THE LIGHT PINK BACKGROUND --- */
    [data-testid="stAppViewContainer"] {
        background-color: #FFF0F3 !important;
    }
    [data-testid="stHeader"] {
        background-color: transparent !important;
    }
    /* Forces regular text to be dark so it's readable on pink */
    .stMarkdown p {
        color: #4A4A4A !important;
    }

    /* --- BUTTON STYLES --- */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3.5em;
        font-size: 16px;
        font-weight: bold;
        background-color: #FFFFFF;
        color: #FB6F92;
        border: 2px solid #FFC2D1;
    }
    .stButton>button:hover {
        background-color: #FFC2D1;
        color: #FFFFFF;
        border: 2px solid #FB6F92;
    }
    .main-title {
        text-align: center;
        color: #000000 !important; /* <--- THIS IS THE LINE TO CHANGE */
        font-family: 'Comic Sans MS', 'Helvetica Neue', sans-serif;
        font-size: 30px;
        margin-bottom: 5px;
    }
    /* --- Fix for Radio Button Text --- */
    div[data-testid="stRadio"] p {
        color: #000000 !important;
        font-weight: bold;
    }
    /* --- Fix for the specific Radio Button Options --- */
    div[role="radiogroup"] label div, 
    div[role="radiogroup"] label p {
        color: #000000 !important;
    }
    /* --- Fix for the specific Radio Button Options (in case they are wrapped in a label) --- */
        color: #FB6F92 !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: #000000; font-family: 'Comic Sans MS', sans-serif; font-size: 32px; margin-bottom: 0px;">
            🎀 Manja Survival Kit 🎀
        </h1>
        <p style="color: #555555; font-size: 15px; margin-top: 5px;">
            Dedicated to my favorite Retail Star • Made by Adam
        </p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# --- MESSAGE DATABASES ---
# You can keep adding inside quotes here until you reach 100! Just make sure each one is in "quotes" and separated by a comma.

clock_in_msgs = [
    "You got this, beautiful! Have a wonderful shift today! ❤️",
    "Go charm those customers and unlock those sales! ✨",
    "Starting the countdown until you are free! Have a great day, sayang.",
    "Another day, another dollar! I know you're going to do great today. 💪",
    "Remember to drink water! Have a super smooth shift! 🚰",
    "You are the star of the AEON branch, don't let anyone tell you otherwise! 🌟",
    "Sending you a big virtual hug to start your shift! 🤗",
    "Time to make that money! Go get 'em, Tya!",
    "I hope today goes by super fast for you! ⏳",
    "Clocking in means you're one step closer to clocking out! 🎉",
    "Have I told you how proud I am of how hard you work? Because I am.",
    "Go sell those 4K displays with that 4K smile! 😁",
    "May your shift be short and your customers be nice today.",
    "You look amazing today, by the way. Go crush it!",
    "Sending good vibes straight to AEON Bukit Tinggi! 📡",
    "Don't work too hard, save some energy for me! 😉",
    "You're going to do amazing today, I just know it.",
    "If anyone gives you trouble, tell them your boyfriend will handle it! 🥊",
    "Just a quick check-in to say I love you and have a great shift! ❤️",
    "May the retail gods bless you with a quiet store today. 🕊️",
    "Step 1: Clock in. Step 2: Be awesome. Step 3: See me! 🏃‍♀️",
    "I believe in you! Even when you don't want to be there.",
    "You've survived 100% of your shifts so far. You'll survive this one too!",
    "Remember, you're the best thing about that mall. 🏬",
    "Have a fantastic day, sayang! I'm cheering for you.",
    "Make sure to sneak a quick break when you can! 🤫",
    "I'm already looking forward to seeing you after work.",
    "I hope you get all the easy, nice customers today.",
    "Take it one hour at a time. You've got this!",
    "You are stronger than the weekend mall crowd! 🦸‍♀️",
    "Just think about the good food we can eat later. 🍔",
    "Your work ethic is seriously inspiring. Go crush it today!",
    "Smile! It confuses the annoying customers. 😏",
    "I'm busy today too, but I'll be doing short check-ins to see how you are! 📱",
    "Don't forget to stretch before standing all day!",
    "You make those uniforms look really good.",
    "May your phone battery last the entire shift! 🔋",
    "Ready, set, sell! You're a natural at this.",
    "Sending a little extra love to get you through the morning.",
    "Whatever happens today, I'm in your corner. 🥊",
    "Today is going to be a good day. Manifesting it for you! ✨",
    "Another shift, another chance to show them how it's done.",
    "Just popping in to remind you that you're my favorite person.",
    "If the store gets too cold, just think warm thoughts! ☕",
    "I'm so lucky to have such a hardworking girl.",
    "Keep calm and sell monitors! 🖥️",
    "I hope time flies by like crazy today. 🦅",
    "You've totally got this under control.",
    "Have a great shift! Text me when you go on break.",
    "Sending you all my energy! ⚡",
    "A brand new shift! Let's make it a good one.",
    "Don't let the mall music drive you crazy today! 🎵",
    "You are capable of handling anything today throws at you.",
    "Just remember, every hour down is a victory.",
    "I love you! Have the best shift possible.",
    "Go show AEON Bukit Tinggi who's boss!",
    "Make sure you eat properly today, okay?",
    "Your smile is going to make someone's day today.",
    "Keep that positive energy up! You're doing great.",
    "I hope your manager is in a good mood today! 😂",
    "You're going to rock this shift.",
    "Another day of being awesome. Let's go!",
    "I'll be thinking about you while you're working.",
    "You bring so much light to that store. 💡",
    "Don't forget how amazing you are, even when it's busy.",
    "Take a deep breath, walk in there, and own the day.",
    "I appreciate everything you do. Have a smooth shift!",
    "You're basically the CEO at this point. 👔",
    "May the time clock move swiftly in your favor.",
    "I hope you get to stand on the soft mats today!",
    "Wishing you zero tech issues and 100% smooth sales.",
    "You're going to do great. I have zero doubts.",
    "Just a sweet reminder that you are loved! ❤️",
    "Have a fantastic shift, my beautiful girl.",
    "Go make that store look good just by being in it.",
    "I'm so proud to call you mine. Have a great day at work!",
    "May your shift be peaceful and drama-free. 🧘‍♀️",
    "You've got the magic touch today, go close those sales!",
    "If you need a distraction later, just press this button again.",
    "I hope the aircon is at the perfect temperature today. ❄️",
    "You are a superstar. Don't forget it!",
    "Sending you a pocketful of sunshine for your shift. ☀️",
    "Let's get this bread! 🍞",
    "I hope you have the most wonderfully boring, easy shift ever.",
    "You're my favorite employee of the month, every month. 🏆",
    "Keep pushing, you're doing an incredible job.",
    "I love your dedication. Have a beautiful day!",
    "Go out there and be the amazing person you are.",
    "Just clocked in? Me too, clocking into missing you! 😉",
    "You've got the brain and the beauty to handle this shift.",
    "I hope your day is as sweet as you are.",
    "Sending a virtual high-five to start the shift right! ✋",
    "You're unstoppable, Tya. Go get 'em!",
    "Have a great shift! Remember, I'm always here if you need me.",
    "You make hard work look so effortless.",
    "Go be the best version of you today!",
    "I'm sending you all the good luck I have. 🍀",
    "Another shift down in the books. Let's do this!",
    "Have a great day at work, sayang! See you later.",
    "Clocked in and ready to win. I believe in you! 🥇"
]

annoying_customer_msgs = [
    "Take a deep breath. Their bad mood has nothing to do with you! 🤫",
    "Just smile, nod, and imagine them tripping on the way out. 😂",
    "Don't let them ruin your vibe! You are doing an amazing job.",
    "Rant to me about them later! For now, just brush it off like a boss. 🛡️",
    "If they only knew how amazing you are! Ignore the haters, sayang. 💅",
    "Customer service is a battlefield, but you are winning. Hang in there! ⚔️",
    "Just imagine me standing behind them making funny faces. 🤪"
     "Some people just wake up choosing violence. Let it slide!",
    "They are temporary, your awesomeness is permanent. ✨",
    "Just pretend you're an NPC and give them the same automated response. 🤖",
    "Their lack of common sense is not your problem!",
    "Breathe in the good vibes, exhale the annoying customer. 🌬️",
    "I'll fight them for you. Just give me the signal! 🥊",
    "Remember, you get to go home and be happy. They have to live with being annoying.",
    "They probably don't even know what a refresh rate is. Ignore them! 📺",
    "You have the patience of a saint. I'm proud of you.",
    "Don't let one bad apple spoil your whole shift.",
    "Just kill them with kindness. It confuses them! 😇",
    "I'm virtually rolling my eyes with you right now. 🙄",
    "Add them to the list of people we are going to gossip about later.",
    "You handled that perfectly, I just know it.",
    "Some customers test our patience so we can level up. Ding! Level up. 🎮",
    "Shake it off! You're way too cool to be stressed by them.",
    "Just picture them as a complaining potato. 🥔",
    "They clearly don't know who they are messing with.",
    "I give you permission to mentally curse them out.",
    "You are a professional. They are just a nuisance.",
    "Let it go, let it go! Don't let them bother you anymore! ❄️",
    "I'm sending a virtual shield to deflect their bad energy. 🛡️",
    "Just nod and think about what you want for dinner. 🍔",
    "Their behavior is a reflection of them, not you.",
    "You are doing great. Some people are just impossible to please.",
    "I bet they couldn't last five minutes doing your job.",
    "Take a 30-second mental vacation. You deserve it. 🏖️",
    "Don't let them live rent-free in your head!",
    "You're a rockstar. That customer was just a backup dancer out of step.",
    "Just remember, the shift will end, but they will always be annoying.",
    "If I was there, I would have totally glared at them for you. 👀",
    "They are the reason retail workers need a medal. 🏅",
    "Deep breaths. Inhale patience, exhale frustration.",
    "You are handling this with so much grace.",
    "Just think, every annoying customer makes a great story for later.",
    "I'll listen to you complain about them for as long as you want later! 🗣️",
    "They're just projecting their bad day onto you. You're fine!",
    "Smile on the outside, screaming on the inside. I get it. 😱",
    "You are so much better than the energy they are bringing.",
    "Just imagine pressing a 'mute' button on them. 🔇",
    "Don't let them dim your sparkle, sayang.",
    "They probably step on Legos in their free time. 🧱",
    "You survived that interaction! Give yourself a mental high five. 🙏",
    "Just focus on the nice customers. Forget that one!",
    "You are the master of customer service. Don't let them shake you.",
    "I wish I could send you a coffee right now to make up for them.",
    "They are entirely unreasonable. You are entirely perfect.",
    "Let's write a one-star review for that customer's personality. ⭐",
    "You have my full permission to take an extra long bathroom break now.",
    "Don't let them ruin your mascara!",
    "They just don't appreciate the PRISM+ aesthetic. Their loss.",
    "Take a deep breath and reset. Next customer!",
    "You handled it like a pro. Keep your head up.",
    "They're just mad they don't have a boyfriend as cool as yours. 😎",
    "You are strong, you are capable, and you are done with them!",
    "Just picture me handing you a trophy for 'Most Patient Girlfriend'. 🏆",
    "They have zero chill, but you have all the chill.",
    "Let's banish them from our thoughts completely. Poof! 💨",
    "You are doing a fantastic job in a tough environment.",
    "They aren't worth your stress lines!",
    "Just think about how good taking your shoes off is going to feel.",
    "Some people belong in a museum for the highly annoying. 🏛️",
    "You are handling the retail trenches like a brave soldier.",
    "Brush it off! Your next customer will be an angel.",
    "They clearly woke up on the wrong side of the bed today.",
    "You are a diamond, they are just a piece of annoying gravel. 💎",
    "I'm proud of you for keeping your cool.",
    "Just imagine throwing a water balloon at them. Splash! 🎈",
    "They don't pay you enough to care about their attitude.",
    "You're too cute to be stressed out by randos.",
    "Let their annoyance bounce right off you.",
    "Take a quick walk to the back room and scream into a box. 📦",
    "You're doing amazing, sweetie! (in the Kris Jenner voice)",
    "They are officially cancelled in our books. 🚫",
    "Don't give them the power to ruin your day.",
    "You have infinite patience. I'm in awe of you.",
    "Just remember: you are right, they are wrong, end of story.",
    "Let it wash over you like water off a duck's back. 🦆",
    "They're just jealous of how good you look in your uniform.",
    "You handled that with 100% professionalism. Go you!",
    "I'll buy you a treat later to make up for that terrible human.",
    "You are the peace amidst their chaos. 🧘‍♀️",
    "Just hit them with the 'Have a nice day' and walk away.",
    "Their negativity has no power here!",
    "You survived the boss battle! 👾",
    "Take a sip of water and wash away the annoyance.",
    "You're a retail warrior. That was just a minor scratch.",
    "They are the glitch in today's matrix. Ignore them. 🖥️",
    "Just laugh at how ridiculous they were being.",
    "You are too precious to be upset by them.",
    "Keep shining, Tya! Don't let them dull you.",
    "I'm sending you a massive wave of calm right now. 🌊",
    "That's over now! Back to being your awesome self."
]

sleepy_msgs = [
    "Sending maximum energy beams your way! ⚡",
    "Hang in there! Sneak away to get a sip of water or stretch a little. 🧘‍♀️",
    "Think about the delicious post-shift food we can get! 🤤",
    "I'm super proud of your hard work today. You can do this!",
    "Virtual Zus Coffee coming right up! ☕ Take a 2-minute mental break.",
    "Splash some water on your face, you're almost at the finish line! 🏁"
      "Wakey wakey! Don't fall asleep on the monitors! 😴",
    "You can sleep all you want when you get home, I promise.",
    "Do 10 jumping jacks in the back room! Just kidding, please don't.",
    "You're doing great! Keep those gorgeous eyes open. 👀",
    "I know it's slow right now, but stay strong!",
    "Just imagine me poking your cheek to keep you awake. 👉",
    "The mall aircon makes everyone sleepy. Fight it!",
    "Think of something really funny to wake your brain up.",
    "You are a machine! Machines don't sleep! 🤖",
    "Go reorganize a shelf, it helps wake the brain up!",
    "Only a little bit longer until you can rest in a real bed. 🛏️",
    "Sending you a digital espresso shot! ☕",
    "You're halfway through the slump! Keep pushing.",
    "I'm sleepy too, we can take a nap together later! 💤",
    "Don't let the sleepiness win! You are a warrior.",
    "Pinch yourself! Not too hard, just a little nip! 🤏",
    "Walk a lap around the store if you can.",
    "You're almost there, sayang. Don't give up now!",
    "Just think about Nasi Lemak to wake up your senses. 🍛",
    "You have my full permission to daydream, just keep your eyes open.",
    "I know you're tired, but you're doing so incredibly well.",
    "Shake it out! Move your arms and wake up that body. 💃",
    "I'm sending you an invisible Red Bull. Drink up! 🥫",
    "Every yawn is just a silent scream for coffee. 🥱",
    "You are powered by pure willpower right now. Impressive!",
    "Look at the bright lights of the PRISM+ TVs to wake up! 💡",
    "Just a little longer! You are a champion of staying awake.",
    "I wish I could be there to keep you entertained and awake.",
    "Try to find the most interesting customer in the store to watch.",
    "You can do this! I believe in your anti-sleep powers.",
    "Go drink some cold water, it shocks the system! 🧊",
    "Think about our next date, that should wake you up! 🥰",
    "You're surviving the hardest part of the shift. Good job!",
    "I'm mentally clapping for you to keep you awake. 👏",
    "Don't close your eyes, it's a trap! 🪤",
    "You are so close to the end, don't let sleep take you now.",
    "I appreciate how hard you're working, even when you're exhausted.",
    "Just imagine a really loud alarm clock going off. ⏰",
    "You are entirely too cute when you're sleepy.",
    "Hold on, Tya! The end of the shift is approaching.",
    "Keep your chin up, literally, so you don't nod off! 😂",
    "I'm sending you a burst of motivation! 💥",
    "You are a professional at looking awake when you're not.",
    "Just think about how good your bed is going to feel tonight.",
    "Fight the urge! You are stronger than the sleepies.",
    "You're doing amazing. Keep fighting the good fight.",
    "I know the retail lighting is hypnotic, but stay with me! 😵‍💫",
    "Go check the back inventory just to walk around.",
    "You have incredible stamina. Keep it up!",
    "Just picture me doing a silly dance for you. 🕺",
    "You're going to sleep so well tonight. Earn it now!",
    "Sending you a wave of fresh, waking energy. 🌬️",
    "You are doing a fantastic job. Don't fall asleep on your feet!",
    "Think of spicy Ayam Gepuk to shock your system awake! 🔥",
    "You've got this! Just a few more hours of staying upright.",
    "I'm so proud of your dedication. Keep those eyes open!",
    "You are a retail superhero. Superheroes don't nap on duty. 🦸‍♀️",
    "Just blink really fast 10 times to reset your eyes! 👁️",
    "You are pushing through like a total boss.",
    "I know it's a drag right now, but I'm cheering you on.",
    "Go wipe down a display monitor, keep those hands moving! 🧽",
    "You are stronger than the mid-shift slump.",
    "I can't wait to see your sleepy face later.",
    "Keep the momentum going! You're doing great.",
    "Just imagine me bringing you your favorite snack. 🍫",
    "You're almost at the finish line. Sprint to the end!",
    "I know you're tired, but your smile is still perfect.",
    "You are doing everything right. Just stay awake!",
    "Take a deep breath of that recycled mall air to wake up! 🏬",
    "You are a legend for pushing through this fatigue.",
    "I'm sending you a jolt of virtual lightning! ⚡",
    "Keep your mind active! Try to do math in your head. ➕",
    "You're surviving the hardest part of the day.",
    "Just think about taking off your work uniform later.",
    "You are doing a brilliant job. Keep holding on!",
    "I'm so impressed by your work ethic, sleepyhead.",
    "Just a little longer! You can do anything for a little longer.",
    "You're my favorite hardworking girl. Keep going!",
    "Don't let the slow hours defeat you!",
    "You are crushing this shift, even if you are half asleep.",
    "I'm right here with you in spirit, keeping you awake.",
    "Go stretch your legs! Walk to the other end of the store. 🚶‍♀️",
    "You are doing an incredible job. Hang in there.",
    "Just imagine me whispering 'wake up' in your ear. 👂",
    "You are completely capable of finishing this shift strong.",
    "I know you're tired, but I'm so proud of you.",
    "Just keep swimming! Or, you know, standing. 🐟",
    "You are doing great. Keep up the amazing work.",
    "I'll have a cozy blanket waiting for you later.",
    "You're almost there! Don't let your eyes betray you now.",
    "You are a superstar for working so hard. Keep it up!",
    "Just a sweet reminder that you are amazing.",
    "Keep fighting the sleep, sayang! You got this.",
    "I'm sending you all the energy I have left today! 💫"
]

feet_hurting_msgs = [
    "Standing all day is truly no joke. 1x Foot Massage Voucher credited! 👣✨",
    "I'll get the massage oil ready for when you're off work! 💆‍♀️",
    "Sit down for 5 minutes if you can! You've earned a rest.",
    "Your hard work doesn't go unnoticed. I appreciate your hustle! ❤️",
    "Just think of how nice taking your shoes off later is going to feel. 👟",
    "You're a champion. Treat yourself to a nice seat during your break! 🪑"
    "Those PRISM+ floors are unforgiving. Hang in there!",
    "I'm mentally rubbing your feet right now. Does it help?",
    "You are walking miles in that store! You're an athlete. 🏃‍♀️",
    "I promise to give your feet the royal treatment later. 👑",
    "Try to shift your weight from foot to foot! Keep the blood flowing.",
    "You're literally standing up for your future. I'm proud of you.",
    "I wish I could bring you some fluffy slippers to wear right now. 🥿",
    "Your poor feet! They are doing a lot of heavy lifting today.",
    "Sit down on a display box if nobody is looking! 📦",
    "You are doing an amazing job. Your feet will forgive you later.",
    "Just imagine soaking your feet in warm water tonight. 🛁",
    "You're a warrior for standing all day. Keep it up!",
    "I'm sending soothing vibes straight to your toes. 〰️",
    "You earn every single ringgit standing on those feet!",
    "If I were there, I'd give you a piggyback ride around the store. 🐷",
    "Take a load off whenever you get the chance. You need it.",
    "Your hard work is so attractive to me. Even your tired feet.",
    "You're doing great! Let's get you a nice foot spa soon.",
    "I know it aches, but you are so strong.",
    "Just a little longer until you can sit down properly.",
    "You are handling this shift like an absolute pro.",
    "I'm adding 'foot rub' to the top of my to-do list for tonight. 📝",
    "You have my deepest sympathies for standing all day.",
    "I'm proud of your endurance. You're doing incredible.",
    "Wiggle your toes to keep them awake! 🦶",
    "You are surviving the hardest part of retail. Good job.",
    "I'll make sure you don't have to lift a finger (or a toe) when you get home.",
    "You are amazing. Keep pushing through the ache.",
    "Just think about how strong your calf muscles are getting! 🦵",
    "You're doing a fantastic job. Hang in there, sayang.",
    "I appreciate all the hard work you put in every day.",
    "You are a superstar for being on your feet this long.",
    "I'm sending a virtual cushion for you to stand on. ☁️",
    "You've totally got this. Ignore the pain, focus on the gain!",
    "You are my favorite hardworking person.",
    "I know it's tough, but you are tougher.",
    "Just imagine me massaging the arches of your feet. Ahh. 😌",
    "You are doing brilliantly. Don't let the sore feet bring you down.",
    "I'll carry you everywhere later if I have to!",
    "You are a champion of endurance. Keep it up.",
    "Sneak to the back and sit down for 60 seconds. I won't tell!",
    "You are crushing this shift. Your feet are just collateral damage.",
    "I'm so impressed by your strength. Keep going!",
    "Just think about putting your feet up on the couch later. 🛋️",
    "You are doing amazing. The foot pain is temporary!",
    "I'm sending healing thoughts to your tired feet.",
    "You are totally allowed to complain about your feet to me later.",
    "I've got the perfect massage technique waiting for you.",
    "You are doing a wonderful job. Keep holding on.",
    "Take a deep breath and push through the soreness.",
    "You're almost at the finish line! Keep standing tall.",
    "I'm so proud of you for working so hard.",
    "You are a hero for enduring the retail floor.",
    "Just imagine soaking them in a warm salt bath. 🧂",
    "You are entirely capable of finishing this shift strong.",
    "I know your feet hurt, but your smile is still radiant.",
    "You are doing a beautiful job today.",
    "I'll have a comfortable spot waiting for you at home.",
    "You are surviving the AEON marathon. Keep going!",
    "I appreciate your dedication so much.",
    "You are a rockstar. Don't let sore feet stop you.",
    "I'm sending you a burst of pain relief energy! 💥",
    "You're doing great. Keep up the amazing work.",
    "I'll pamper you so much later, I promise.",
    "You are a trooper for dealing with this every shift.",
    "Just a sweet reminder that you are doing an incredible job.",
    "I know it hurts, but I'm right here cheering you on.",
    "You are my favorite person, even with sore feet.",
    "Keep pushing, you're doing an amazing job.",
    "I'm so lucky to have such a resilient girl.",
    "You are doing fantastic. Hang in there!",
    "I'll make sure you can completely relax later.",
    "You are a powerhouse. Keep standing strong.",
    "Just think about the moment you finally get to sit in the car.",
    "You are doing a brilliant job in a tough environment.",
    "I'm sending you all my love to help you push through.",
    "You are amazing. Keep up the good work.",
    "I'll give you a foot rub that will make you forget the entire shift.",
    "You are a superstar for being on your feet this long.",
    "I know it's hard, but you are doing wonderfully.",
    "You're almost there! Don't give up now.",
    "I appreciate everything you do. Have a smooth rest of the shift!",
    "You are doing great. Just keep breathing.",
    "I'm so proud of your hard work. Keep it up!",
    "You are my hardworking queen. 👑",
    "Just imagine taking off your socks, the best feeling ever! 🧦",
    "You are doing amazing. Keep fighting the good fight.",
    "I'm sending you a massive wave of comfort right now.",
    "You are entirely too cute to be in pain.",
    "Keep shining, Tya! You've got this.",
    "I'll have the hot water ready for a foot soak later.",
    "You are a retail warrior. Keep going strong.",
    "I know your feet are screaming, but you are winning.",
    "Just a little longer and you can finally rest. Love you! ❤️"
]


# --- SECTION 1: THE MOOD BOOSTER ---
st.markdown("<h3 style='color: #FB6F92;'>📋 How's the shift going, sayang?</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Just Clocked In"):
        st.toast("You got this!", icon="✨")
        st.info(random.choice(clock_in_msgs))

    if st.button("😤 Annoying Customer"):
        st.toast("Shrug it off!", icon="🤫")
        st.warning(random.choice(annoying_customer_msgs))

with col2:
    if st.button("🥱 Battling Sleepiness"):
        st.toast("Energy incoming!", icon="⚡")
        st.error(random.choice(sleepy_msgs))

    if st.button("🦶 Feet Are Hurting"):
        st.toast("Voucher activated!", icon="💆‍♀️")
        st.success(random.choice(feet_hurting_msgs))

st.divider()

# --- SECTION 2: LUNCH BREAK ROULETTE ---
st.markdown("<h3 style='color: #FB6F92;'>🍴 Lunch Break Roulette</h3>", unsafe_allow_html=True)
st.write("Don't waste your precious break time deciding what to eat. Let the app handle it!")

# --- FOOD DATABASES ---
full_break_food = [
    "Chicken Rice Shop 🍗 (Classic and filling!)",
    "Ayam Gepuk Tokmat 🔥 (Ready for that spicy kick?)",
    "Sambal Buka Baju 🌶️ (Pedas gila but so worth it!)",
    "Nasi Goreng 🍛 (Comfort food time)",
    "Nasi Kerabu 🥗 (Fresh and sedap!)",
    "Larkin 🍲",
    "Mee Goreng 🍝",
    "Kueh Teow Goreng 🍜",
    "Subway 🥪 (Make it a footlong!)",
    "Zus Coffee + a nice pastry ☕🥐"
    "Grilled Chicken Chop w/ Mushroom Sauce 🥩 (Savory, zero spice, total comfort)",
    "Garlic Butter Lamb Chops 🍖 (A premium treat for my hardworking girl!)",
    "Clear Soup Pan Mee / Udon 🍜 (Warm and soothing for the throat)",
    "Teppanyaki 🍳 (Hot, garlicky, and super satisfying)",
]

quick_break_food = [
    "Strawberry 🍓 (Sweet, light, and perfect for a quick 15-30 min break!)",
    "Zus Coffee ☕ (Quick grab & go for maximum energy!)",
    "Subway 🥪 (Fast, fresh, and easy to eat fast!)",
    "Quick tapau of Nasi Goreng 🍛",
    "Quick tapau of Mee Goreng 🍝"
    "Empire Sushi 🍣 (Grab a few pieces, zero mess, super fast!)",
    "llaollao Froyo 🍦 (Cold, sweet, and a perfect refreshing reset!)",
    "Auntie Anne's Pretzel + Lemonade 🥨 (The ultimate quick mall snack!)",
]

time_available = st.radio("How much time do you have?", ["Full Lunch Break (1 Hour)", "Quick Rush (15-30 Mins)"])

if st.button("🎲 Spin for Food!", type="primary"):
    st.balloons()
    
    # Logic to pick the right menu based on her time
    if "Quick" in time_available:
        selected_food = random.choice(quick_break_food)
        st.markdown("### 📍 Your Quick Match:")
        st.info(f"**{selected_food}** \n\n*Grab it fast and enjoy your quick rest! 🏃‍♀️💨*")
    else:
        selected_food = random.choice(full_break_food)
        st.markdown("### 📍 Your Match for Today:")
        st.success(f"**{selected_food}**! \n\n*Go grab your food, sit down, and enjoy every minute of your break. 😋*")

st.divider()

# --- FOOTER ---
st.markdown("<p style='text-align: center; color: #FFB3C6; font-size: 13px; font-weight: bold;'>Made with love • Always just a text away if you need me 🥰</p>", unsafe_allow_html=True)
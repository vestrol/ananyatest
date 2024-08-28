import streamlit as st
import numpy as np
import joblib
from google.cloud import firestore
from google.oauth2 import service_account
import time

# Authenticate to Firestore with the JSON account key.
import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="test-855c2")

# Create a reference to the Google post.
doc_ref = db.collection("post").document("test")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())

st.set_page_config(layout="wide")

tab1, tab2, tab3, tab4, tab5, tab6= st.tabs(["Home", "Screening Quiz", "More Information", "Donate", "About me + Contact Us", "Q&A"])
data = np.random.randn(10, 1)

@st.cache_resource
def load_model():
	mod = joblib.load('best_random_forest_model.joblib')
	return mod
	
def set_language(tab_number, languages_key):
    if f"selected_language{tab_number}" in st.session_state:
        lang = st.session_state[f"selected_language{tab_number}"]
        st.experimental_set_query_params(**{f"lang{tab_number}": languages_key[lang]})
        return lang
    return "English"
	
with tab1:
	engInfo = "English"
	spanInfo = "Spanish"
	hindiInfo = "Hindi"
	languages = {"English": engInfo, "Spanish": spanInfo, "Hindi": hindiInfo}

	sel_lang1 = st.radio(
        	"Language",
        	options=languages.keys(),
        	horizontal=True,
        	key="selected_language1",
    	)
	selected_language1 = set_language(1, languages)
	
	st.markdown(f"Selected Language: {selected_language1}")
	if selected_language1 == "English":
		st.subheader("What is Obstructive Sleep Apnea?")
		st.write("")
		col = st.columns(2)
		with col[0]:
			st.write("Obstructive sleep apnea (OSA) is a prevalent sleep disorder characterized by repeated interruptions in breathing during sleep. These interruptions occur when the muscles in the throat relax excessively, causing the airway to narrow or close partially or completely. As a result, the flow of air into the lungs is restricted, leading to brief pauses in breathing. These pauses can occur numerous times throughout the night, disrupting the normal sleep cycle and leading to fragmented and poor-quality sleep.")
			st.write("")
			st.write("The most common symptom of obstructive sleep apnea is loud and persistent snoring. Other symptoms include pauses in breathing during sleep, often witnessed by a bed partner, and gasping or choking sensations as breathing resumes. Individuals with OSA may also experience daytime symptoms such as excessive daytime sleepiness, morning headaches, difficulty concentrating, and irritability. Furthermore, OSA can lead to nocturnal symptoms such as frequent awakenings, night sweats, and a dry or sore throat upon waking.")
			st.image('apneapic.png')
		with col[1]:
			st.image('https://sleepapneatreatment.com/wp-content/uploads/2022/10/Obstructive-Sleep-Apnea.gif')
			st.write("Untreated, obstructive sleep apnea can have serious health consequences. The repeated interruptions in breathing lead to oxygen desaturation, putting strain on the cardiovascular system and increasing the risk of hypertension, heart disease, and stroke. OSA is also associated with metabolic disorders such as insulin resistance and type 2 diabetes. Additionally, untreated OSA can contribute to daytime fatigue, impairing cognitive function and increasing the risk of accidents while driving or operating machinery. Moreover, the chronic sleep disruption associated with OSA can negatively impact mood, leading to depression and anxiety in some individuals.")
		st.write("---")
	if selected_language1 == "Spanish":
		st.subheader("¿Qué es la apnea obstructiva del sueño?")
		st.write("")
		col = st.columns(2)
		with col[0]:
			st.write("La apnea obstructiva del sueño (AOS) es un trastorno del sueño frecuente que se caracteriza por interrupciones repetidas de la respiración durante el sueño. Estas interrupciones ocurren cuando los músculos de la garganta se relajan excesivamente, lo que hace que las vías respiratorias se estrechen o se cierren parcial o completamente. Como Como resultado, el flujo de aire hacia los pulmones se restringe, lo que provoca breves pausas en la respiración. Estas pausas pueden ocurrir numerosas veces durante la noche, interrumpiendo el ciclo normal del sueño y provocando un sueño fragmentado y de mala calidad.")
			st.write("")
			st.write("El síntoma más común de la apnea obstructiva del sueño son los ronquidos fuertes y persistentes. Otros síntomas incluyen pausas en la respiración durante el sueño, a menudo presenciadas por un compañero de cama, y ​​sensaciones de jadeo o asfixia a medida que se reanuda la respiración. Las personas con AOS también pueden experimentar síntomas diurnos como somnolencia diurna excesiva, dolores de cabeza matutinos, dificultad para concentrarse e irritabilidad. Además, la AOS puede provocar síntomas nocturnos como despertares frecuentes, sudores nocturnos y garganta seca o dolor al despertar.")
			st.image('apneapic.png')
		with col[1]:
			st.image('https://sleepapneatreatment.com/wp-content/uploads/2022/10/Obstructive-Sleep-Apnea.gif')
			st.write("La apnea obstructiva del sueño no tratada puede tener graves consecuencias para la salud. Las repetidas interrupciones de la respiración provocan una desaturación de oxígeno, lo que ejerce presión sobre el sistema cardiovascular y aumenta el riesgo de hipertensión, enfermedades cardíacas y accidentes cerebrovasculares. La AOS también se asocia con trastornos metabólicos como la resistencia a la insulina y la diabetes tipo 2. Además, la AOS no tratada puede contribuir a la fatiga diurna, perjudicando la función cognitiva y aumentando el riesgo de accidentes al conducir o utilizar maquinaria. Además, la interrupción crónica del sueño asociada con la AOS puede afectar negativamente el estado de ánimo y provocar depresión y ansiedad en algunas personas.")
		st.write("---")
	if selected_language1 == "Hindi":
		st.subheader("ऑब्सट्रक्टिव स्लीप एपनिया क्या है?")
		st.write("")
		col = st.columns(2)
		with col[0]:
			st.write("ऑब्सट्रक्टिव स्लीप एपनिया का सबसे आम लक्षण जोर से और लगातार खर्राटे लेना है। अन्य लक्षणों में नींद के दौरान सांस लेने में रुकावट शामिल है, जिसे अक्सर बिस्तर पर साथी द्वारा देखा जाता है, और सांस फिर से शुरू होने पर हांफने या दम घुटने की अनुभूति होती है। ओएसए से पीड़ित व्यक्तियों को दिन में अत्यधिक नींद आना, सुबह सिरदर्द, ध्यान केंद्रित करने में कठिनाई और चिड़चिड़ापन जैसे लक्षणों का भी अनुभव हो सकता है। इसके अलावा, ओएसए रात में लक्षण पैदा कर सकता है जैसे बार-बार जागना, रात में पसीना आना और जागने पर गला सूखना या दर्द होना।")
			st.write("")
			st.write("ऑब्सट्रक्टिव स्लीप एपनिया का सबसे आम लक्षण जोर से और लगातार खर्राटे लेना है। अन्य लक्षणों में नींद के दौरान सांस लेने में रुकावट शामिल है, जिसे अक्सर बिस्तर पर साथी द्वारा देखा जाता है, और सांस फिर से शुरू होने पर हांफने या दम घुटने की अनुभूति होती है। ओएसए से पीड़ित व्यक्तियों को दिन में अत्यधिक नींद आना, सुबह सिरदर्द, ध्यान केंद्रित करने में कठिनाई और चिड़चिड़ापन जैसे लक्षणों का भी अनुभव हो सकता है। इसके अलावा, ओएसए रात में लक्षण पैदा कर सकता है जैसे बार-बार जागना, रात में पसीना आना और जागने पर गला सूखना या दर्द होना।")
			st.image('apneapic.png')
		with col[1]:
			st.image('https://sleepapneatreatment.com/wp-content/uploads/2022/10/Obstructive-Sleep-Apnea.gif')
			st.write("अनुपचारित, ऑब्सट्रक्टिव स्लीप एपनिया के गंभीर स्वास्थ्य परिणाम हो सकते हैं। सांस लेने में बार-बार रुकावट से ऑक्सीजन की कमी हो जाती है, जिससे हृदय प्रणाली पर दबाव पड़ता है और उच्च रक्तचाप, हृदय रोग और स्ट्रोक का खतरा बढ़ जाता है। ओएसए इंसुलिन प्रतिरोध और टाइप 2 मधुमेह जैसे चयापचय संबंधी विकारों से भी जुड़ा है। इसके अतिरिक्त, अनुपचारित ओएसए दिन के समय थकान, संज्ञानात्मक कार्य को ख़राब कर सकता है और ड्राइविंग या मशीनरी चलाते समय दुर्घटनाओं के जोखिम को बढ़ा सकता है। इसके अलावा, ओएसए से जुड़ी पुरानी नींद की गड़बड़ी मूड पर नकारात्मक प्रभाव डाल सकती है, जिससे कुछ व्यक्तियों में अवसाद और चिंता हो सकती है।")
		st.write("---")
	
with tab2:
	st.header("Get your screening results today!")
	with st.form("my_form"):
		name = st.text_input("Please enter your name (first is fine)")
		contact = st.text_input("Please enter a form of contact i.e. email, phone, etc.")
		with st.expander("What is your gender by birth?"):
			gender = st.radio("", ["male", "female"])
		age = st.slider('What is your age?', 18, 100)
		sle = st.slider("On average, what is your daily sleep duration in hours?", 1, 24)
		weight = st.slider("How much do you weigh? in lbs", 80, 300)
		height = st.slider("How tall are you? in inches", 48, 84)
		sbp = st.number_input("What is your Systolic blood pressure?", step=1)
		dbp = st.number_input("What is your Diastolic blood pressure?", step=1)
		hr = st.number_input("What is your heart rate?", step=1)
		steps = st.number_input("On average, how many steps do you take in a day?", step=1)
		physical = st.number_input("On average, how many minutes do you workout in a day?", step=1)

		"""For the following questions, answer on a scale of 0-5 about the last month, where 0 = never, 1 = 1-3 days, 2 = ~1 day per week, 3 = 2-4 nights per week, 4 = 5-6 nights per week, and 5 = almost every night"""
		qs1 = st.slider("Experienced difficulty falling asleep?", 0, 5)
		qs2 = st.slider("Woken up at night and easily fell asleep again?", 0, 5)
		qs3 = st.slider("Woken up and had difficulty falling asleep again / difficulty staying asleep?", 0, 5)
		qs4 = st.slider("Non-restorative sleep? i.e. feeling tired or worn-out after getting a usual amount of sleep", 0, 5)

		"""For the following questions, answer on a scale of 0-4 about the last month, where 0 = never, 1 = almost never, 2 = sometimes, 3 = fairly often, and 4 = very often"""
		sl1 = st.slider("How often have you been upset because of something that happened unexpectedly?", 0, 4)
		sl2 = st.slider("How often have you felt that you were unable to control the important things in your life?", 0, 4)
		sl3 = st.slider("How often have you felt nervous and stressed?", 0, 4)
		sl4 = st.slider("How often have you felt confident about your ability to handle your personal problems?", 0, 4)
		sl5 = st.slider("How often have you felt that things were going your way?", 0, 4)
		sl6 = st.slider("How often have you found that you could not cope with all the things that you had to do?", 0, 4)
		sl7 = st.slider("How often have you been able to control irritations in your life?", 0, 4)
		sl8 = st.slider("How often have you felt that you were on top of things?", 0, 4)
		sl9 = st.slider("How often have you been angered because of things that happened that were outside of your control?", 0, 4)
		sl10 = st.slider("How often have you felt difficulties were piling up so high that you could not overcome them?", 0, 4)
			  
		sub = st.form_submit_button('Submit')
		if sub:
			qs = (qs1+qs2+qs3+qs4)//2
			sl = (sl1+sl2+sl3+(4-sl4)+(4-sl5)+sl6+(4-sl7)+(4-sl8)+sl9+sl10)//4
			bmi = (weight/(height**2)) * 703
			if bmi < 18.5:
				bm = 0
			elif bmi >= 18.5 and bmi < 25:
				bm = 1
			elif bmi >= 25 and bmi < 30:
				bm = 2
			else:
				bm = 3
			if gender == 'female':
				gn = 0
			else:
				gn = 1
			inp = [[gn,age,sle,qs,physical,sl,bm,hr,steps,sbp,dbp]]
			model = load_model()
			new = model.predict(inp)
			prediction = ""
			if new == 0:
				st.write("You have a healthy sleep")
				prediction = "healthy"
			elif new == 1:
				st.write("You might have Insomnia, please visit a doctor")
				prediction = "insomnia"
			elif new == 2:
				st.write("You might have Sleep Apnea, please visit a doctor")
				prediction = "sleep apnea"
			ts = time.time()
			ts = str(ts).split('.')[0]
			# This time, we're creating a NEW post reference for Apple
			doc_ref = db.collection("userData").document(ts)
			
			# And then uploading some data to that reference
			doc_ref.set({
				"username": name,
				"contact": contact,
				"age": age,
				"sleep duration": sle,
				"weight": weight,
				"height": height,
				"systolic bp": sbp,
				"diastolic bp": dbp,
				"heart rate": hr,
				"daily steps": steps,
				"daily physical activity": physical,
				"JSS1": qs1,
				"JSS2": qs2,
				"JSS3": qs3,
				"JSS4": qs4,
				"PSS1": sl1,
				"PSS2": sl2,
				"PSS3": sl3,
				"PSS4": sl4,
				"PSS5": sl5,
				"PSS6": sl6,
				"PSS7": sl7,
				"PSS8": sl8,
				"PSS9": sl9,
				"PSS10": sl10,
				"prediction": prediction
			})

with tab3:
	st.subheader("Find out more about OSA")
	col3 = st.columns(2)
	with col3[0]: 	
		st.write("To find out more about OSA, check out our YouTube channel and our FaceBook blog! We post informative videos about all aspects of OSA and hope to spread awareness about this silent killer. ")
		st.video('https://youtu.be/IIKlqbLwS7M')
		st.video('https://youtu.be/KGEKz4r5n8Q?si=thuPAv_9QfiZTaEP')
	with col3[1]:
		post_urls = [
			'<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid02tm8fT82sxZorg5KeE4DLSVC4nAM5Z2kFY7vss3R4Z5jtRLet8EJ53xDbbB8mZSuEl%26id%3D61560444242747&show_text=true&width=500" width="500" height="250" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>'
			'<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid02xn5PEUKkp7UADruTUYGTqYsVSgCPJjsN3Se7ZHPwkjvSoR8NZucpHE5nrSAmUt7el%26id%3D61560444242747&show_text=true&width=500" width="500" height="636" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>'
			'<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid065hjmMpZJZqgmd2xsMe4VxPgGbUVD5WAzasrZ6VWWoz7349VByDM4uVUTQbx6qz9l%26id%3D61560444242747&show_text=true&width=500" width="500" height="661" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>'
			'<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid0AYK4p3PmqkLpUTaEcgVGL3iDWNgGrSb6FbPVLqZkokWfcZqEG2kTjdypgw9zeqL9l%26id%3D61560444242747&show_text=true&width=500" width="500" height="661" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>'
			'<iframe src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fpermalink.php%3Fstory_fbid%3Dpfbid0V9JrMdpByR4bmZYR9aCD42gToQjaVgbD5zM8CaGbhgZWcouNFzGZN48FwrpAhdPdl%26id%3D61560444242747&show_text=true&width=500" width="500" height="622" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"></iframe>'
			# Add more URLs as needed
		]
		
		def embed_facebook_post(post_url):
		    embed_code = post_url
		    st.markdown(embed_code, unsafe_allow_html=True)

		for url in post_urls:
    			embed_facebook_post(url)

with tab4:
	st.header("Join the Against Obstructive Sleep Apnea by Donating Now!")
	col1, col2 = st.columns([0.38, 0.62])
	
	with col1:
		gofundme_url = "https://www.gofundme.com/f/join-the-fight-against-sleep-apnea/widget/medium?sharesheet=CAMPAIGN_PAGE&attribution_id=sl:b1feb9fb-cbab-4945-af87-4c4286a75742"
		
		gofundme_iframe = f'''
		<iframe
		  src="{gofundme_url}"
		  style="height: 180px; width: 100%;"
		  frameborder="0"
		  scrolling="yes"
		></iframe>
		'''
		st.markdown(gofundme_iframe, unsafe_allow_html=True)

		youtube_url1 = "https://www.youtube.com/embed/g665P3z8sGk"
		youtube_iframe1 = f'''
		<iframe
		  width="100%"
		  height="300"
		  src="{youtube_url1}"
		  frameborder="0"
		  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
		  allowfullscreen
		></iframe>
		'''
		st.markdown(youtube_iframe1, unsafe_allow_html=True)
		
	with col2:
		youtube_url2 = "https://www.youtube.com/embed/eKItaKdLxPA?si=VTXdSF4Jmd0XQ5oY"
		youtube_iframe2 = f'''
		<iframe
		  width="100%"
		  height="450"
		  src="{youtube_url2}"
		  frameborder="0"
		  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
		  allowfullscreen
		></iframe>
		'''
		st.markdown(youtube_iframe2, unsafe_allow_html=True)
			  
with tab5:	
	engInfo4 = "English"
	spanInfo4 = "Spanish"
	hindiInfo4 = "Hindi"
	languages4 = {"English": engInfo4, "Spanish": spanInfo4, "Hindi": hindiInfo4}

	sel_lang4 = st.radio(
		"Language",
	        options=languages4.keys(),
	        horizontal=True,
	        key="selected_language4",
	)
	selected_language4 = set_language(4, languages4)
	
	st.markdown(f"Selected Language: {selected_language4}")
	col4 = st.columns(2)
	if selected_language4 == "English":
		with col4[0]:
			st.subheader("About Me")
			st.write("Hello! I am Ananya Aggarwal, a highschooler in Fremont, CA. I started this project to raise awareness about obstructive sleep apnea, an extrmemly widespread sleep disorder around the world. I was shocked by the number of my own family members and friends who were affected by the disorder and realized the problem is much bigger than expected. After doing research about OSA and its treatments, I realized that a big contributing factor to the lack of patient diagnosis for OSA is the expense and inavailblity of its diagnosis options. The most common diagnosis option for OSA, sleep tests, are expensive and not always easy to access, making it hard for possible OSA pateints to seek early diagnosis and therefore more effective treatment. My intelligent OSA screenoing quiz briges this gap between suspecting patients and professional diagnosis. The quiz is free to all and available on all web browsers. It currently predicts whether a user has healthy sleep or is at risk for either OSA or insomnia. I plan to enhance the quiz to also provide users with a prediction of how at-risk/likely they are to have obstructive sleep apnea, informing them of whether they are should get checked for it soon. My goals with this project are to raise the awareness for OSA in general and to gain popularity for my quiz to provide a free first step to OSA patients' diagnosis and treatment journey!")
		with col4[1]:
			st.subheader("Contact Us")
			st.write("Contact us here!")
			st.link_button("Click here to find all my links & forms of contact!", "https://linktr.ee/apneaast")
			st.link_button("YouTube", "https://youtube.com/@apneaassist?si=aWi0IgocfLbwCBuZ")
			st.link_button("FaceBook", "https://www.facebook.com/profile.php?id=61560444242747")
			st.link_button("GoFundMe", "https://gofund.me/6858e97d")
			st.write("Email: apneaassist@gmail.com")
	elif selected_language4 == "Spanish":
		with col4[0]:
			st.subheader("Acerca de Mí")
			st.write("¡Hola! Soy Ananya Aggarwal, estudiante de secundaria en Fremont, CA. Comencé este proyecto para crear conciencia sobre la apnea obstructiva del sueño, un trastorno del sueño extremadamente extendido en todo el mundo. Me sorprendió la cantidad de familiares y amigos afectados por el trastorno y me di cuenta de que el problema es mucho mayor de lo esperado. Después de investigar sobre la AOS y sus tratamientos, me di cuenta de que un factor que contribuye en gran medida a la falta de diagnóstico de AOS en los pacientes es el costo y la indisponibilidad de sus opciones de diagnóstico. La opción de diagnóstico más común para la AOS, las pruebas del sueño, son costosas y no siempre de fácil acceso, lo que dificulta que los posibles pacientes con AOS busquen un diagnóstico temprano y, por lo tanto, un tratamiento más eficaz. Mi cuestionario inteligente de detección de AOS cierra esta brecha entre los pacientes sospechosos y el diagnóstico profesional. El cuestionario es gratuito para todos y está disponible en todos los navegadores web. Actualmente predice si un usuario tiene un sueño saludable o si tiene riesgo de sufrir AOS o insomnio. Planeo mejorar el cuestionario para brindarles a los usuarios una predicción sobre el riesgo o la probabilidad de que tengan apnea obstructiva del sueño, informándoles si deben hacerse un examen pronto. Mis objetivos con este proyecto son crear conciencia sobre la AOS en general y ganar popularidad para mi cuestionario para proporcionar un primer paso gratuito en el diagnóstico y tratamiento de los pacientes con AOS.")
		with col4[1]:
			st.subheader("Contacta con Nosotras")
			st.write("Contacta con nosotras aquí!")
			st.link_button("¡Haz click aquí para encontrar todos mis enlaces y formas de contacto!", "https://linktr.ee/apneaast")
			st.link_button("YouTube", "https://youtube.com/@apneaassist?si=aWi0IgocfLbwCBuZ")
			st.link_button("FaceBook", "https://www.facebook.com/profile.php?id=61560444242747")
			st.link_button("GoFundMe", "https://gofund.me/6858e97d")
			st.write("Email: apneaassist@gmail.com")
	elif selected_language4 == "Hindi":
		with col4[0]:
			st.subheader("मेरे बारे में")
			st.write("नमस्ते! मैं अनन्या अग्रवाल हूं, फ़्रेमोंट, सीए में हाई स्कूल की छात्रा। मैंने यह परियोजना ऑब्सट्रक्टिव स्लीप एपनिया, एक नींद विकार जो दुनिया भर में बेहद व्यापक है, के बारे में जागरूकता बढ़ाने के लिए शुरू की है। मैं इस विकार से प्रभावित परिवार और दोस्तों की संख्या से आश्चर्यचकित था और मुझे एहसास हुआ कि समस्या अपेक्षा से कहीं अधिक बड़ी है। ओएसए और इसके उपचारों पर शोध करने के बाद, मुझे एहसास हुआ कि रोगियों में ओएसए का निदान न हो पाने का एक बड़ा कारण उनके निदान विकल्पों की लागत और अनुपलब्धता है। ओएसए के लिए सबसे आम निदान विकल्प, नींद परीक्षण, महंगा है और हमेशा आसानी से उपलब्ध नहीं होता है, जिससे संभावित ओएसए रोगियों के लिए शीघ्र निदान और इसलिए अधिक प्रभावी उपचार प्राप्त करना मुश्किल हो जाता है। मेरी स्मार्ट ओएसए स्क्रीनिंग प्रश्नावली संदिग्ध रोगियों और पेशेवर निदान के बीच इस अंतर को बंद कर देती है। क्विज़ सभी के लिए मुफ़्त है और सभी वेब ब्राउज़र पर उपलब्ध है। यह वर्तमान में भविष्यवाणी करता है कि क्या उपयोगकर्ता को स्वस्थ नींद आती है या उसे ओएसए या अनिद्रा का खतरा है। मैं उपयोगकर्ताओं को उनके जोखिम या ऑब्सट्रक्टिव स्लीप एपनिया होने की संभावना के बारे में पूर्वानुमान देने के लिए प्रश्नावली में सुधार करने की योजना बना रहा हूं, जिससे उन्हें पता चल सके कि क्या उन्हें जल्द ही परीक्षण करवाना चाहिए। इस परियोजना के साथ मेरा लक्ष्य सामान्य रूप से ओएसए के बारे में जागरूकता बढ़ाना और ओएसए रोगियों के निदान और उपचार में मुफ्त पहला कदम प्रदान करने के लिए मेरी प्रश्नावली के लिए लोकप्रियता हासिल करना है।")
		with col4[1]:
			st.subheader("संपर्क करें")
			st.write("हमसे यहां संपर्क करें!")
			st.link_button("मेरे सभी लिंक और संपर्क फ़ॉर्म पाने के लिए यहां क्लिक करें!", "https://linktr.ee/apneaast")
			st.link_button("यूट्यूब", "https://youtube.com/@apneaassist?si=aWi0IgocfLbwCBuZ")
			st.link_button("फेसबुक", "https://www.facebook.com/profile.php?id=61560444242747")
			st.link_button("गोफंडमी", "https://gofund.me/6858e97d")
			st.write("ईमेल: apneaassist@gmail.com")

with tab6:
	engInfo6 = "English"
	spanInfo6 = "Spanish"
	hindiInfo6 = "Hindi"
	languages6 = {"English": engInfo6, "Spanish": spanInfo6, "Hindi": hindiInfo6}

	sel_lang6 = st.radio(
		"Language",
	        options=languages6.keys(),
	        horizontal=True,
	        key="selected_language6",
	)
	selected_language6 = set_language(6, languages6)
	
	st.markdown(f"Selected Language: {selected_language6}")
	if selected_language6 == "English":
		st.subheader("Have questions? Check here!")
		st.write("Find answers to your questions about OSA and about Apnea Assist! If you can't find an answer here, please let me know by typing it in the feedback form below.")
		st.write("General Questions about OSA")
		with st.expander("What is Obstructive Sleep Apnea (OSA)?"):
			st.write("OSA is a sleep disorder where the airway becomes blocked during sleep, causing breathing to stop and start repeatedly.")
		with st.expander("What causes OSA?"):
			st.write("OSA is often caused by the relaxation of throat muscles, excess weight, and anatomical factors like a large neck or tonsils.")
		with st.expander("What are the common symptoms of OSA?"):
			st.write("Common symptoms include loud snoring, daytime fatigue, morning headaches, and waking up gasping for air.")
		with st.expander("How is OSA diagnosed?"):
			st.write("OSA is diagnosed through a sleep study, either at a clinic or using a home sleep test that monitors breathing patterns.")	
		with st.expander("Who is most at risk for developing OSA?"):
			st.write("Risk factors include being overweight, having a family history of OSA, being male, and being over 40, though anyone can develop it.")	
		with st.expander("Can children have OSA?"):
			st.write("Yes, children can have OSA, often due to enlarged tonsils or adenoids, and it can affect their growth and development.")
		with st.expander("What are the long-term health risks of untreated OSA?"):
			st.write("Untreated OSA can lead to serious health issues like heart disease, stroke, high blood pressure, and diabetes.")
		with st.expander("Is OSA hereditary"):
			st.write("Yes, there can be a genetic predisposition to OSA, especially related to anatomical traits.")
		with st.expander("What lifestyle changes can help manage OSA?"):
			st.write("Losing weight, avoiding alcohol before bed, quitting smoking, and changing sleep positions can help manage OSA.")
		with st.expander("How does OSA affect daily life and overall well-being?"):
			st.write("OSA can cause chronic fatigue, poor concentration, mood swings, and decreased overall quality of life.")
		with st.expander("Is OSA a common condition?"):
			st.write("Yes, OSA is relatively common, affecting an estimated 3-7% of adults, though many cases go undiagnosed.")
		with st.expander("Can OSA be cured?"):
			st.write("OSA is a chronic condition, however, if diagnosed early, it can be effectively managed with lifestyle changes, CPAP therapy, or surgery.")
		with st.expander("How does OSA differ from other sleep disorders like insomnia?"):
			st.write("OSA is a breathing disorder during sleep, while insomnia is the inability to fall or stay asleep.")
		with st.expander("Are there any specific sleeping positions that help with OSA?"):
			st.write("Sleeping on your side instead of your back can help reduce OSA symptoms.")
		with st.expander("What is the difference between OSA and central sleep apnea?"):
			st.write("OSA is caused by a physical blockage of the airway, while central sleep apnea is due to the brain not sending proper signals to breathe.")
		with st.expander("What are the biggest misconceptions about OSA?"):
			st.write("A common misconception is that OSA only affects older, overweight men, when in fact, it can affect anyone, including women and children.")
		
		st.write("Questions About Diagnosis and Management Options")
		with st.expander("What are the different methods for diagnosing OSA?"):
			st.write("Diagnosis methods include in-lab sleep studies and home sleep apnea tests, both of which monitor your sleep and breathing.")
		with st.expander("How does a sleep study work?"):
			st.write("During a sleep study, sensors track your breathing, oxygen levels, heart rate, and sleep stages to diagnose OSA.")
		with st.expander("What is a home sleep test, and how accurate is it?"):
			st.write("A home sleep test is a simplified version of a sleep study that you do at home; it’s accurate for diagnosing moderate to severe OSA.")
		with st.expander("What are the treatment options for OSA?"):
			st.write("Treatment options include CPAP therapy, oral appliances, lifestyle changes, and in some cases, surgery.")
		with st.expander("How does a CPAP machine work?"):
			st.write("A CPAP machine keeps your airway open by delivering a constant stream of air through a mask while you sleep.")
		with st.expander("Are there alternatives to CPAP therapy?"):
			st.write("Yes, alternatives include oral appliances, weight loss, positional therapy, and surgery in some cases.")
		with st.expander("Can lifestyle changes alone manage OSA?"):
			st.write("Lifestyle changes can help mild cases, but moderate to severe OSA usually requires medical treatment.")
		with st.expander("What is the role of surgery in treating OSA?"):
			st.write("Surgery may be an option if other treatments fail, and it involves removing or altering tissue in the airway.")
		with st.expander("How effective are dental devices in managing OSA?"):
			st.write("Dental devices can be effective for mild to moderate OSA by repositioning the jaw to keep the airway open.")
		with st.expander("What is the cost of getting diagnosed and treated for OSA?"):
			st.write("Costs vary widely depending on insurance coverage, the type of test, and treatment, but many options are available to reduce out-of-pocket expenses.")
		with st.expander("How often should someone with OSA see a doctor?"):
			st.write("Regular follow-ups, usually once a year or more if symptoms change, are recommended for ongoing management.")
		with st.expander("What is the success rate of OSA treatments?"):
			st.write("Treatment success varies, but CPAP and other therapies are highly effective when used consistently.")
		with st.expander("Can OSA symptoms improve without medical intervention?"):
			st.write("Mild symptoms may improve with lifestyle changes, but medical intervention is often necessary for effective management.")
		with st.expander("Are there any new treatments or technologies for OSA?"):
			st.write("New treatments include advanced CPAP machines, implantable devices like Inspire, and ongoing research into less invasive options.")
		with st.expander("How does weight loss impact OSA?"):
			st.write("Weight loss can significantly reduce OSA severity by decreasing the amount of tissue that obstructs the airway.")
		with st.expander("What other resources do you recommend for someone newly diagnosed with OSA?"):
			st.write("We recommend consulting a sleep specialist and exploring reputable sources like the American Academy of Sleep Medicine.")
		
		st.write("Questions About Apnea Assist")
		with st.expander("What is Apnea Assist?"):
			st.write("Apnea Assist is a platform dedicated to raising awareness about OSA and providing resources, including an intelligent screening quiz and educational content.")
		with st.expander("How does your intelligent screening quiz work?"):
			st.write("Our quiz uses AI/ML models to assess your risk of OSA, based on your responses to a series of health-related questions.")
		with st.expander("Is the screening quiz on Apnea Assist accurate?"):
			st.write("Yes, it’s designed to be more accurate than traditional tools by incorporating a broader range of data points.")
		with st.expander("What makes Apnea Assist different from other OSA resources?"):
			st.write("Apnea Assist combines advanced screening tools with comprehensive educational content and community support.")
		with st.expander("Is Apnea Assist affiliated with any medical institutions?"):
			st.write("We are an independent platform, but we base our resources and tools on scientifically validated research and expert input.")
		with st.expander("How can Apnea Assist help me if I suspect I have OSA?"):
			st.write("Take our screening quiz, explore educational resources, and connect with healthcare professionals for further evaluation.")
		with st.expander("Do you offer personalized recommendations after the screening quiz?"):
			st.write("Based on your quiz results, we provide  advice and next steps for managing your risk. We are working on providng more personalized support for each of our users.")
		with st.expander("How often is the content on Apnea Assist updated?"):
			st.write("We regularly update our content to reflect the latest research and developments in OSA treatment and management.")
		with st.expander("Can I trust the information on Apnea Assist?"):
			st.write("Yes, our content is carefully curated and based on reliable, scientifically-backed sources.")
		with st.expander("Is Apnea Assist free to use?"):
			st.write("Yes, our platform is free to access, including the screening quiz and all educational materials.")
		with st.expander("How do you protect the privacy of users on Apnea Assist?"):
			st.write("Personal information is not required to submit the screening form and is only used to contact users with additional materials based on their quiz results.")
		with st.expander("Are there any upcoming features or tools on Apnea Assist?"):
			st.write("Yes, we are planning to expand our tools, including a mobile app, more interactive content, and additional world languages.")
		with st.expander("How do I sign up for updates or newsletters from Apnea Assist?"):
			st.write("You can follow our Facebook account and subscribe to our YouTube! Both links can we found by scanning thr QR code on the 'contact us' page.")
		with st.expander("Can I contribute or share my story on Apnea Assist?"):
			st.write("We are currently working on setting up a community blog on our website, but in the mean time, feel free to post comments to any of our content on other platforms!")
		with st.expander("How can I support Apnea Assist’s mission?"):
			st.write("You can support us by spreading the word, donating to our gofundme, and participating in our events and campaigns. Reach out to learn more!")
		with st.expander("Is Apnea Assist working with any partners or organizations?"):
			st.write("We’re in the process of building partnerships with healthcare providers and organizations to broaden our reach and impact.")
		with st.expander("How is Apnea Assist funded?"):
			st.write("Apnea Assist is funded through generound donations on our gofundme, please visit our 'Donate' page to learn more and support our cause!")
		with st.expander("What feedback have you received from users?"):
			st.write("Users have appreciated the accessibility and accuracy of our tools, as well as the comprehensive educational content.")
		with st.expander("Can I speak with someone who has used Apnea Assist?"):
			st.write("While we don’t share personal contacts, we are working setting up a community blog page where users can post testimonials and find support.")
		with st.expander("How can I share Apnea Assist with others?"):
			st.write("You can share our website link or out QR code, share our YouTube vidoes and Facebook blogs, or use social media to spread the word.")
		with st.expander("How can healthcare providers collaborate with Apnea Assist?"):
			st.write("We welcome collaborations with healthcare providers to integrate our tools into their practices and improve patient care.")
		with st.expander("Can Apnea Assist be used by healthcare professionals for their patients?"):
			st.write("Yes, healthcare professionals can use our screening tools and resources to assist in diagnosing and managing OSA. We hope that doctors recommend Apnea Assist as a first step in at-risk patients' journey with diagnosing OSA.")
		with st.expander("What role does technology play in Apnea Assist?"):
			st.write("Technology, particularly AI/ML, is central to our platform, helping us provide more accurate screenings and personalized recommendations.")
		with st.expander("Is there a mobile app for Apnea Assist?"):
			st.write("We’re currently developing a mobile app to make our tools even more accessible.")
		with st.expander("Can Apnea Assist help with other sleep disorders?"):
			st.write("While our focus is on OSA, some of our resources and tips may be helpful for managing other sleep disorders.")
	
		st.header(":mailbox: Questions or Comments? Get In Touch With Me!")
		contact_form = """
		<form action="https://formsubmit.co/apneaassist@gmail.com" method="POST">
	 	    <input type="hidden" name="_captcha" value="false">
		     <input type="text" name="name" placeholder="Your name" required>
		     <input type="email" name="email" placeholder="Your email" required>
		     <textarea name="message" placeholder="Your message here"></textarea>
	             <input type="hidden" name="_next" value="https://apneaassist.streamlit.app/?lang4=English#find-out-more-about-osa">
		     <button type="submit">Send</button>
		</form>
	 	"""
			
		st.markdown(contact_form, unsafe_allow_html=True)
		# Use Local CSS File
		def local_css(file_name):
		    with open(file_name) as f:
		        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
		
		
		local_css("style/style.css")
		
	if selected_language6 == "Spanish":
		st.subheader("¿Tienes preguntas? ¡Consulta aquí!")
		st.write("Encuentra respuestas a tus preguntas sobre la apnea obstructiva del sueño (AOS) y sobre Apnea Assist. Si no puedes encontrar una respuesta aquí, por favor házmelo saber llenando el formulario de comentarios a continuación.")
		st.write("Preguntas Generales sobre AOS")
		with st.expander("¿Qué es la apnea obstructiva del sueño (AOS)?"):
			st.write("AOS es un trastorno del sueño donde las vías respiratorias se bloquean durante el sueño, causando que la respiración se detenga y reinicie repetidamente.")
		with st.expander("¿Qué causa la AOS?"):
			st.write("La AOS es causada por la relajación de los músculos de la garganta, el exceso de peso y factores anatómicos como un cuello grande o amígdalas grandes.")
		with st.expander("¿Cuáles son los síntomas comunes de la AOS?"):
			st.write("Los síntomas comunes incluyen ronquidos fuertes, fatiga diurna, dolores de cabeza matutinos y despertarse con sensación de ahogo.")
		with st.expander("¿Cómo se diagnostica la AOS?"):
			st.write("La AOS se diagnostica a través de un estudio del sueño, ya sea en una clínica o utilizando una prueba de sueño en casa que monitorea los patrones de respiración.")	
		with st.expander("¿Quién está más en riesgo de desarrollar AOS?"):
			st.write("Los factores de riesgo incluyen el sobrepeso, tener antecedentes familiares de AOS, ser hombre y tener más de 40 años, aunque cualquiera puede desarrollarlo.")	
		with st.expander("¿Los niños pueden tener AOS?"):
			st.write("Sí, los niños pueden tener AOS, a menudo debido a amígdalas o adenoides agrandadas, y puede afectar su crecimiento y desarrollo.")
		with st.expander("¿Cuáles son los riesgos para la salud a largo plazo de no tratar la AOS?"):
			st.write("No tratar la AOS puede llevar a problemas de salud graves como enfermedades cardíacas, derrames cerebrales, hipertensión y diabetes.")
		with st.expander("¿Es la AOS hereditaria?"):
			st.write("Sí, puede haber una predisposición genética a la AOS, especialmente relacionada con características anatómicas.")
		with st.expander("¿Qué cambios en el estilo de vida pueden ayudar a manejar la AOS?"):
			st.write("Perder peso, evitar el alcohol antes de dormir, dejar de fumar y cambiar las posiciones de sueño pueden ayudar a manejar la AOS.")
		with st.expander("¿Cómo afecta la AOS la vida diaria y el bienestar general?"):
			st.write("La AOS puede causar fatiga crónica, mala concentración, cambios de humor y una disminución de la calidad de vida en general.")
		with st.expander("¿Es la AOS una condición común?"):
			st.write("Sí, la AOS es relativamente común, afectando a un estimado de 3-7% de los adultos, aunque muchos casos no se diagnostican.")
		with st.expander("¿La AOS se puede curar?"):
			st.write("La AOS es una condición crónica, sin embargo, si se diagnostica temprano, puede ser manejada efectivamente con cambios en el estilo de vida, terapia CPAP o cirugía.")
		with st.expander("¿Cómo se diferencia la AOS de otros trastornos del sueño como el insomnio?"):
			st.write("La AOS es un trastorno respiratorio durante el sueño, mientras que el insomnio es la incapacidad de conciliar o mantener el sueño.")
		with st.expander("¿Hay alguna posición específica para dormir que ayude con la AOS?"):
			st.write("Dormir de lado en lugar de boca arriba puede ayudar a reducir los síntomas de la AOS.")
		with st.expander("¿Cuál es la diferencia entre la AOS y la apnea central del sueño?"):
			st.write("La AOS es causada por un bloqueo físico de las vías respiratorias, mientras que la apnea central del sueño se debe a que el cerebro no envía señales adecuadas para respirar.")
		with st.expander("¿Cuáles son los mayores conceptos erróneos sobre la AOS?"):
			st.write("Un concepto erróneo común es que la AOS solo afecta a hombres mayores con sobrepeso, cuando en realidad, puede afectar a cualquier persona, incluidos mujeres y niños.")
		
		st.write("Preguntas Sobre Diagnóstico y Opciones de Tratamiento")
		with st.expander("¿Cuáles son los diferentes métodos para diagnosticar la AOS?"):
			st.write("Los métodos de diagnóstico incluyen estudios de sueño en laboratorio y pruebas de apnea del sueño en casa, ambos monitorean tu sueño y respiración.")
		with st.expander("¿Cómo funciona un estudio del sueño?"):
			st.write("Durante un estudio del sueño, se utilizan sensores para rastrear la respiración, los niveles de oxígeno, la frecuencia cardíaca y las etapas del sueño para diagnosticar la AOS.")
		with st.expander("¿Qué es una prueba de sueño en casa y qué tan precisa es?"):
			st.write("Una prueba de sueño en casa es una versión simplificada de un estudio del sueño que se realiza en casa; es precisa para diagnosticar la AOS moderada a severa.")
		with st.expander("¿Cuáles son las opciones de tratamiento para la AOS?"):
			st.write("Las opciones de tratamiento incluyen la terapia CPAP, aparatos orales, cambios en el estilo de vida y, en algunos casos, cirugía.")
		with st.expander("¿Cómo funciona una máquina CPAP?"):
			st.write("Una máquina CPAP mantiene las vías respiratorias abiertas al proporcionar un flujo constante de aire a través de una mascarilla mientras duermes.")
		with st.expander("¿Existen alternativas a la terapia CPAP?"):
			st.write("Sí, las alternativas incluyen aparatos orales, pérdida de peso, terapia de posición y cirugía en algunos casos.")
		with st.expander("¿Pueden los cambios en el estilo de vida manejar la AOS por sí solos?"):
			st.write("Los cambios en el estilo de vida pueden ayudar en casos leves, pero la AOS moderada a severa generalmente requiere tratamiento médico.")
		with st.expander("¿Cuál es el papel de la cirugía en el tratamiento de la AOS?"):
			st.write("La cirugía puede ser una opción si otros tratamientos fallan, e implica la eliminación o alteración de tejido en las vías respiratorias.")
		with st.expander("¿Qué tan efectivos son los dispositivos dentales en el manejo de la AOS?"):
			st.write("Los dispositivos dentales pueden ser efectivos para la AOS leve a moderada al reposicionar la mandíbula para mantener las vías respiratorias abiertas.")
		with st.expander("¿Cuál es el costo de diagnosticar y tratar la AOS?"):
			st.write("Los costos varían ampliamente según la cobertura de seguro, el tipo de prueba y tratamiento, pero existen muchas opciones disponibles para reducir los gastos de bolsillo.")
		with st.expander("¿Con qué frecuencia debe ver a un médico una persona con AOS?"):
			st.write("Se recomiendan seguimientos regulares, generalmente una vez al año o más si los síntomas cambian, para el manejo continuo.")
		with st.expander("¿Cuál es la tasa de éxito de los tratamientos para la AOS?"):
			st.write("El éxito del tratamiento varía, pero la terapia CPAP y otros tratamientos son altamente efectivos cuando se usan de manera consistente.")
		with st.expander("¿Pueden mejorar los síntomas de la AOS sin intervención médica?"):
			st.write("Los síntomas leves pueden mejorar con cambios en el estilo de vida, pero la intervención médica es a menudo necesaria para un manejo efectivo.")
		with st.expander("¿Existen nuevos tratamientos o tecnologías para la AOS?"):
			st.write("Los nuevos tratamientos incluyen máquinas CPAP avanzadas, dispositivos implantables como Inspire, e investigaciones en curso sobre opciones menos invasivas.")
		with st.expander("¿Cómo impacta la pérdida de peso en la AOS?"):
			st.write("La pérdida de peso puede reducir significativamente la gravedad de la AOS al disminuir la cantidad de tejido que obstruye las vías respiratorias.")
		with st.expander("¿Qué otros recursos recomiendas para alguien recién diagnosticado con AOS?"):
			st.write("Recomendamos consultar a un especialista en sueño y explorar fuentes confiables como la Academia Americana de Medicina del Sueño.")
		
		st.write("Preguntas Sobre Apnea Assist")
		with st.expander("¿Qué es Apnea Assist?"):
			st.write("Apnea Assist es una plataforma dedicada a aumentar la conciencia sobre la AOS y proporcionar recursos, incluyendo un cuestionario de detección inteligente y contenido educativo.")
		with st.expander("¿Cómo funciona tu cuestionario de detección inteligente?"):
			st.write("Nuestro cuestionario utiliza modelos de IA/ML para evaluar tu riesgo de AOS, basándose en tus respuestas a una serie de preguntas relacionadas con la salud.")
		with st.expander("¿Es preciso el cuestionario de detección en Apnea Assist?"):
			st.write("Sí, está diseñado para ser más preciso que las herramientas tradicionales al incorporar una gama más amplia de puntos de datos.")
		with st.expander("¿Qué hace que Apnea Assist sea diferente de otros recursos sobre la AOS?"):
			st.write("Apnea Assist combina herramientas de detección avanzadas con contenido educativo integral y apoyo comunitario.")
		with st.expander("¿Apnea Assist está afiliada a alguna institución médica?"):
			st.write("Somos una plataforma independiente, pero basamos nuestros recursos y herramientas en investigaciones científicas validadas y la opinión de expertos.")
		with st.expander("¿Cómo puede ayudarme Apnea Assist si sospecho que tengo AOS?"):
			st.write("Toma nuestro cuestionario de detección, explora los recursos educativos y consulta a un profesional médico para obtener más orientación.")
		with st.expander("¿Apnea Assist proporciona tratamiento o diagnóstico de AOS?"):
			st.write("No, pero proporcionamos herramientas para evaluar tu riesgo y recursos para ayudarte a encontrar el tratamiento adecuado.")
		with st.expander("¿Cuál es la misión de Apnea Assist?"):
			st.write("Nuestra misión es empoderar a las personas con conocimiento sobre la AOS y proporcionar recursos para una intervención temprana y un tratamiento eficaz.")
		with st.expander("¿Puedo confiar en la información proporcionada en Apnea Assist?"):
			st.write("Sí, toda nuestra información se basa en investigaciones científicas y ha sido revisada por expertos en la materia.")
		with st.expander("¿Cómo mantiene Apnea Assist la privacidad del usuario?"):
			st.write("Priorizamos la privacidad del usuario y seguimos las mejores prácticas para proteger tus datos personales.")
		with st.expander("¿Qué tipo de contenido encuentro en Apnea Assist?"):
			st.write("Ofrecemos una combinación de artículos educativos, videos informativos, y herramientas interactivas como nuestro cuestionario de detección.")

	
		st.header(":mailbox: ¿Preguntas o comentarios? ¡Ponte en contacto conmigo!")
		contact_form = """
		<form action="https://formsubmit.co/apneaassist@gmail.com" method="POST">
	 	    <input type="hidden" name="_captcha" value="false">
		     <input type="text" name="name" placeholder="Su nombre" required>
		     <input type="email" name="email" placeholder="Tu correo electrónico" required>
		     <textarea name="message" placeholder="Tu mensaje aquí"></textarea>
	             <input type="hidden" name="_next" value="https://apneaassist.streamlit.app/?lang4=English#find-out-more-about-osa">
		     <button type="submit">Send</button>
		</form>
	 	"""
			
		st.markdown(contact_form, unsafe_allow_html=True)
		# Use Local CSS File
		def local_css(file_name):
		    with open(file_name) as f:
		        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
		local_css("style/style.css")

	if selected_language6 == "Hindi":
		st.subheader("कोई सवाल है? यहाँ पूछें!")
		st.write("अपनी ऑब्सट्रक्टिव स्लीप एपनिया (OSA) और अप्निया असिस्ट से संबंधित सवालों के जवाब यहाँ पाएं। अगर आपको यहाँ जवाब नहीं मिलता है, तो कृपया नीचे दिए गए फीडबैक फॉर्म को भरकर मुझे बताएं।")
		st.write("OSA के सामान्य प्रश्न")
		with st.expander("ऑब्सट्रक्टिव स्लीप एपनिया (OSA) क्या है?"):
			st.write("OSA एक नींद विकार है जिसमें सोते समय वायुमार्ग अवरुद्ध हो जाते हैं, जिससे श्वास रुक जाती है और बार-बार फिर से शुरू हो जाती है।")
		with st.expander("OSA का कारण क्या है?"):
			st.write("OSA का कारण गले के मांसपेशियों का शिथिल होना, अधिक वजन और कुछ शारीरिक संरचना जैसे बड़ा गला या बड़ी टॉन्सिल्स होते हैं।")
		with st.expander("OSA के सामान्य लक्षण क्या हैं?"):
			st.write("सामान्य लक्षणों में जोर से खर्राटे लेना, दिन में थकान, सुबह सिरदर्द और सांस घुटने की भावना के साथ जागना शामिल हैं।")
		with st.expander("OSA का निदान कैसे किया जाता है?"):
			st.write("OSA का निदान नींद के अध्ययन के माध्यम से किया जाता है, जो कि एक क्लिनिक में या घर पर किए जाने वाले स्लीप टेस्ट द्वारा किया जाता है।")	
		with st.expander("OSA विकसित करने का जोखिम किन्हें होता है?"):
			st.write("जोखिम कारकों में अधिक वजन, OSA का पारिवारिक इतिहास, पुरुष होना, और 40 साल से अधिक उम्र शामिल हैं, हालांकि कोई भी इसे विकसित कर सकता है।")	
		with st.expander("क्या बच्चों को भी OSA हो सकता है?"):
			st.write("हाँ, बच्चों को भी OSA हो सकता है, अक्सर इसका कारण बड़ी टॉन्सिल्स या एडेनॉइड्स होते हैं, और यह उनके विकास और विकास को प्रभावित कर सकता है।")
		with st.expander("OSA का इलाज न कराने के दीर्घकालिक स्वास्थ्य जोखिम क्या हैं?"):
			st.write("OSA का इलाज न कराने से गंभीर स्वास्थ्य समस्याएं हो सकती हैं, जैसे हृदय रोग, स्ट्रोक, उच्च रक्तचाप, और मधुमेह।")
		with st.expander("क्या OSA अनुवांशिक है?"):
			st.write("हाँ, OSA के लिए एक आनुवंशिक प्रवृत्ति हो सकती है, विशेष रूप से शारीरिक संरचना से संबंधित विशेषताओं से।")
		with st.expander("OSA को प्रबंधित करने के लिए कौन से जीवनशैली में बदलाव मदद कर सकते हैं?"):
			st.write("वजन घटाना, सोने से पहले शराब से बचना, धूम्रपान छोड़ना और सोने की स्थिति बदलना OSA को प्रबंधित करने में मदद कर सकते हैं।")
		with st.expander("OSA दैनिक जीवन और समग्र कल्याण को कैसे प्रभावित करता है?"):
			st.write("OSA से लगातार थकान, खराब एकाग्रता, मूड में बदलाव और समग्र जीवन की गुणवत्ता में गिरावट हो सकती है।")
		with st.expander("क्या OSA एक सामान्य स्थिति है?"):
			st.write("हाँ, OSA अपेक्षाकृत सामान्य है, जिससे अनुमानित 3-7% वयस्क प्रभावित होते हैं, हालांकि कई मामलों का निदान नहीं होता है।")
		with st.expander("क्या OSA को ठीक किया जा सकता है?"):
			st.write("OSA एक दीर्घकालिक स्थिति है, लेकिन अगर इसका जल्दी निदान किया जाता है, तो इसे जीवनशैली में बदलाव, CPAP थेरेपी या सर्जरी के साथ प्रभावी ढंग से प्रबंधित किया जा सकता है।")
		with st.expander("OSA अन्य नींद विकारों जैसे अनिद्रा से कैसे अलग है?"):
			st.write("OSA एक श्वसन नींद विकार है, जबकि अनिद्रा नींद न आना या सोने में कठिनाई के रूप में जानी जाती है।")
		with st.expander("क्या कोई विशेष सोने की स्थिति है जो OSA के लिए मददगार हो?"):
			st.write("पीठ के बल सोने की बजाय बाईं या दाईं ओर सोने से OSA के लक्षण कम हो सकते हैं।")
		with st.expander("OSA और सेंट्रल स्लीप एपनिया में क्या अंतर है?"):
			st.write("OSA शारीरिक अवरोध के कारण होता है, जबकि सेंट्रल स्लीप एपनिया मस्तिष्क से श्वास के लिए उचित संकेत न मिलने के कारण होता है।")
		with st.expander("OSA के बारे में सबसे बड़े मिथक क्या हैं?"):
			st.write("एक सामान्य मिथक यह है कि OSA केवल वृद्ध पुरुषों को प्रभावित करता है, जबकि वास्तव में, यह किसी को भी प्रभावित कर सकता है, जिसमें महिलाएं और बच्चे भी शामिल हैं।")
		
		st.write("निदान और उपचार विकल्पों के बारे में प्रश्न")
		with st.expander("OSA के निदान के विभिन्न तरीके क्या हैं?"):
			st.write("निदान के तरीके में प्रयोगशाला में नींद अध्ययन और घरेलू स्लीप एपनिया परीक्षण शामिल हैं, दोनों ही आपकी नींद और श्वास की निगरानी करते हैं।")
		with st.expander("नींद का अध्ययन कैसे काम करता है?"):
			st.write("नींद के अध्ययन के दौरान, श्वास, ऑक्सीजन स्तर, हृदय गति और नींद के चरणों को ट्रैक करने के लिए सेंसर का उपयोग किया जाता है, जिससे OSA का निदान होता है।")
		with st.expander("एक घरेलू स्लीप टेस्ट क्या है और यह कितना सटीक है?"):
			st.write("एक घरेलू स्लीप टेस्ट एक सरल संस्करण है जिसे घर पर किया जाता है; यह मध्यम से गंभीर OSA के निदान में सटीक है।")
		with st.expander("OSA के उपचार के विकल्प क्या हैं?"):
			st.write("उपचार विकल्पों में CPAP थेरेपी, ओरल अप्लायंसेज, जीवनशैली में बदलाव और कुछ मामलों में सर्जरी शामिल है।")
		with st.expander("एक CPAP मशीन कैसे काम करती है?"):
			st.write("CPAP मशीन नींद के दौरान एक मास्क के माध्यम से वायुमार्ग को खुला रखने के लिए निरंतर हवा का प्रवाह प्रदान करती है।")
		with st.expander("क्या CPAP थेरेपी के विकल्प मौजूद हैं?"):
			st.write("हाँ, विकल्पों में ओरल अप्लायंसेज, वजन घटाना, स्थिति थेरेपी और कुछ मामलों में सर्जरी शामिल हैं।")
		with st.expander("क्या जीवनशैली में बदलाव अकेले OSA को प्रबंधित कर सकते हैं?"):
			st.write("जीवनशैली में बदलाव हल्के मामलों में मदद कर सकते हैं, लेकिन मध्यम से गंभीर OSA के लिए आमतौर पर चिकित्सा उपचार की आवश्यकता होती है।")
		with st.expander("OSA के उपचार में सर्जरी की क्या भूमिका है?"):
			st.write("अगर अन्य उपचार विफल हो जाते हैं, तो सर्जरी एक विकल्प हो सकती है, जिसमें वायुमार्ग में ऊतक को हटाने या बदलने की प्रक्रिया शामिल है।")
		with st.expander("OSA के प्रबंधन में दंत उपकरण कितने प्रभावी हैं?"):
			st.write("दंत उपकरण हल्के से मध्यम OSA के लिए प्रभावी हो सकते हैं, जो वायुमार्ग को खुला रखने के लिए जबड़े को पुनः स्थिति में रखते हैं।")
		with st.expander("OSA के निदान और उपचार की लागत क्या है?"):
			st.write("लागत व्यापक रूप से बीमा कवरेज, परीक्षण के प्रकार और उपचार के अनुसार भिन्न होती है, लेकिन खर्च को कम करने के लिए कई विकल्प उपलब्ध हैं।")
		with st.expander("OSA से पीड़ित व्यक्ति को कितनी बार डॉक्टर को दिखाना चाहिए?"):
			st.write("नियमित फॉलो-अप की सिफारिश की जाती है, आमतौर पर साल में एक बार या अगर लक्षण बदलते हैं, तो इससे अधिक बार, प्रबंधन के लिए।")
		with st.expander("OSA के उपचार की सफलता दर क्या है?"):
			st.write("उपचार की सफलता भिन्न होती है, लेकिन CPAP थेरेपी और अन्य उपचार नियमित उपयोग के साथ अत्यधिक प्रभावी होते हैं।")
		with st.expander("क्या OSA के लक्षण बिना चिकित्सा हस्तक्षेप के सुधर सकते हैं?"):
			st.write("हल्के लक्षण जीवनशैली में बदलाव से सुधर सकते हैं, लेकिन प्रभावी प्रबंधन के लिए चिकित्सा हस्तक्षेप की अक्सर आवश्यकता होती है।")
		with st.expander("OSA के लिए कोई नए उपचार या तकनीकें हैं?"):
			st.write("नए उपचार में उन्नत CPAP मशीनें, Inspire जैसे इम्प्लांटेबल डिवाइस और कम आक्रामक विकल्पों पर चल रहे अनुसंधान शामिल हैं।")
		with st.expander("OSA पर वजन घटाने का क्या प्रभाव पड़ता है?"):
			st.write("वजन घटाने से वायुमार्ग को अवरुद्ध करने वाले ऊतक की मात्रा कम हो जाती है, जिससे OSA की गंभीरता काफी हद तक कम हो सकती है।")
		with st.expander("OSA के हाल में निदान किए गए व्यक्ति के लिए आप किन अन्य संसाधनों की सलाह देते हैं?"):
			st.write("हम एक नींद विशेषज्ञ से परामर्श करने और अमेरिकन एकेडमी ऑफ स्लीप मेडिसिन जैसे विश्वसनीय स्रोतों का")

	
		st.header(":mailbox: प्रश्न या टिप्पणियाँ? मेरे संपर्क में रहें!")
		contact_form = """
		<form action="https://formsubmit.co/apneaassist@gmail.com" method="POST">
	 	    <input type="hidden" name="_captcha" value="false">
		     <input type="text" name="name" placeholder="आपका नाम" required>
		     <input type="email" name="email" placeholder="आपका ईमेल" required>
		     <textarea name="message" placeholder="आपका सन्देश यहां"></textarea>
	             <input type="hidden" name="_next" value="https://apneaassist.streamlit.app/?lang4=English#find-out-more-about-osa">
		     <button type="submit">Send</button>
		</form>
	 	"""
			
		st.markdown(contact_form, unsafe_allow_html=True)
		# Use Local CSS File
		def local_css(file_name):
		    with open(file_name) as f:
		        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
		
		
		local_css("style/style.css")
		



	
	




  

			 

	

    



			


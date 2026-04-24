# 📖 User Manual: Exploring Gemma 4 E4B

[🇺🇸 English](#-user-manual-exploring-gemma-4-e4b) | [🇸🇦 العربية](#-دليل-المستخدم-استكشاف-gemma-4-e4b)

---

Welcome to the **Gemma 4 Data Assistant**! This demo is designed to push the boundaries of what a local, 4-billion parameter model can do. Use this guide to experience the "Wow" factors.

---

## 📂 Step 1: Ingesting Data
1. Ensure your `llama-server` is active with multimodal support.
    * **QUICK START:** Run the **`llama-opencode.bat`** file in the project folder. It is optimized for RTX 4060 8GB with flash attention and KV cache quantization.
2. Drag and drop any **CSV** or **Excel** file into the sidebar.
3. **Watch the Sidebar:** The **🩺 Gemma Data Health Check** will instantly profile your data, and the **Context Usage** meter will show you how much of the 128K window is being used.

---

## 🧪 Step 2: Try the "Wow" Scenarios

### 🔬 Scenario A: The Deep Reasoner
1. Set the **Reasoning Depth** slider to **"Deep Analysis"**.
2. Ask: *"If we double the salary of the bottom 5 employees and fire the top earner, how does our monthly average change? Think step-by-step."*
3. **The Wow:** Open the `🤔 View AI Reasoning` tab to watch Gemma "write notes" to itself and verify its math before answering.

### 🎙️ Scenario B: Voice to Data
1. Click the **Microphone icon** in the chat bar.
2. Say: *"Gemma, who is the manager for the IT department?"*
3. **The Wow:** Gemma transcribes your voice locally using its native ASR — no internet required.

### 💾 Scenario C: AI-Generated Excel Reports
1. Type: *"Create an Excel report with a summary table and a bar chart of sales by department."*
2. **The Wow:** The AI writes Python code using openpyxl to build a formatted Excel workbook. A **📥 Download Excel Report** button appears — click to save the report!

### 📊 Scenario D: The Agentic Visualization
1. Type: *"Draw a colorful pie chart showing employee distribution by department."*
2. **The Wow:** The AI will decide to use its `execute_python_code` tool. You will see the Python code appear, followed by a beautiful chart rendered directly in the chat.

### 📋 Scenario E: Data Transformation & Export
1. Type: *"Filter the data to show only 'Active' employees in the 'Finance' department making more than $1,500."*
2. **The Wow:** Gemma will create a **📋 Result Table** in the chat. Underneath it, a button will appear: **"💾 Download this X row result"**. Click it to save your filtered data as a new Excel file!

---

## ⚙️ Pro Configuration
- **Quick Mode:** Use this for simple lookups. It stops the model from "overthinking" and saves time.
- **Vision Uploads:** You can upload an image of a chart or a screenshot from a different system and ask: *"How does the trend in this picture compare to my current Excel file?"*

---

## 🔒 Privacy Notice
**This is a 100% local demo.** 
Your data is processed entirely by the model running in your terminal. No data, audio, or images are ever uploaded to the cloud or sent to Google. 

---
### About the Developer
This project was developed by **Mahamed Algaroshy**, an electrical engineer and AI enthusiast who develops software that involves AI tools to help people in their lives.

---

<br><br>

# 📖 دليل المستخدم: استكشاف Gemma 4 E4B

مرحباً بك في **مساعد بيانات Gemma 4**! هذا العرض مصمم لاختبار قدرات نموذج 4 مليار معلمة محلي. استخدم هذا الدليل لتجربة عوامل الإبهار.

---

## 📂 الخطوة 1: تحميل البيانات
1. تأكد من أن `llama-server` يعمل مع دعم الوسائط المتعددة.
    * **البدء السريع:** شغّل ملف **`llama-opencode.bat`** في مجلد المشروع. إنه مُحسّن لـ RTX 4060 8GB مع flash attention وضغط KV cache.
2. اسحب وأفلت أي ملف **CSV** أو **Excel** إلى الشريط الجانبي.
3. **راقب الشريط الجانبي:** سيقوم **🩺 فحص صحة البيانات** بتحليل بياناتك فوراً، وسيظهر **عداد السياق** كم استهلكت من نافذة 128K.

---

## 🧪 الخطوة 2: جرب سيناريوهات الإبهار

### 🔬 السيناريو أ: المُفكّر العميق
1. اضبط شريط **عمق التفكير** على **"تحليل عميق"**.
2. اسأل: *"إذا ضاعفنا راتب أقل 5 موظفين وطردنا الأعلى أجراً، كيف يتغير متوسط الرواتب الشهري؟ فكّر خطوة بخطوة."*
3. **الإبهار:** افتح تبويب `🤔 عرض طريقة التفكير` لتشاهد Gemma وهو "يكتب ملاحظات" لنفسه ويتحقق من حساباته قبل الإجابة.

### 🎙️ السيناريو ب: الصوت إلى بيانات
1. انقر على **أيقونة الميكروفون** في شريط الدردشة.
2. قل: *"ما هو متوسط الرواتب حسب القسم؟"*
3. **الإبهار:** Gemma يحوّل صوتك إلى نص باستخدام التعرف الصوتي الأصلي — بدون إنترنت.

### 💾 السيناريو ج: تقارير Excel الذكية
1. اكتب: *"أنشئ تقرير Excel يحتوي على جدول ملخص ورسم بياني شريطي للمبيعات حسب القسم."*
2. **الإبهار:** الذكاء الاصطناعي يكتب كود Python باستخدام openpyxl لبناء ملف Excel منسق. زر **📥 تحميل تقرير Excel** يظهر — انقر لحفظ التقرير!

### 📊 السيناريو د: التصور الذكي
1. اكتب: *"ارسم مخططاً دائرياً ملوناً يظهر توزيع الموظفين حسب القسم."*
2. **الإبهار:** الذكاء الاصطناعي يستخدم أداة `execute_python_code`. ستشاهد كود Python يظهر، متبوعاً برسم بياني جميل يظهر في الدردشة مباشرة.

### 📋 السيناريو هـ: تحويل البيانات والتصدير
1. اكتب: *"صفي البيانات لإظهار الموظفين 'النشطين' في قسم 'المالية' الذين يتقاضون أكثر من 1,500."*
2. **الإبهار:** Gemma سينشئ **📋 جدول النتائج** في الدردشة. سيظهر زر **"💾 تحميل نتيجة الـ X صف"**. انقر لتحفظ بياناتك المصفاة كملف Excel!

---

## ⚙️ إعدادات متقدمة
- **الوضع السريع:** استخدمه للاستعلامات البسيطة. يمنع النموذج من "الإفراط في التفكير" ويوفر الوقت.
- **رفع الصور:** يمكنك رفع صورة لرسم بياني أو لقطة شاشة من نظام آخر واسأل: *"كيف يقارن الاتجاه في هذه الصورة بملف Excel الحالي؟"*

---

## 🔒 إشعار الخصوصية
**هذا عرض 100% محلي.**
جميع بياناتك تُعالج بالكامل بواسطة النموذج الذي يعمل على جهازك. لا يتم رفع أي بيانات أو صوت أو صور إلى السحابة أو إرسالها إلى Google.

---

### عن المطور
تم تطوير هذا المشروع بواسطة **ماهر القروشي**، مهندس كهربائي ومطور ذكاء اصطناعي يطور برمجيات تستخدم أدوات الذكاء الاصطناعي لمساعدة الناس في حياتهم.

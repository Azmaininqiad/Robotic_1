```diff
--- a/app.py
+++ b/app.py
@@ -1,3 +1,55 @@
-from flask import Flask
+import os
+from flask import Flask, request, render_template
+from werkzeug.utils import secure_filename
 
-app = Flask(__name__)
+app = Flask(__name__)
+
+UPLOAD_FOLDER = 'uploads'
+app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
+
+ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}
+
+def allowed_file(filename):
+    return '.' in filename and \
+           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
+
+@app.route('/', methods=['GET', 'POST'])
+def upload_files():
+    if request.method == 'POST':
+        name = request.form['name']
+        image = request.files['image']
+        pdf = request.files['pdf']
+
+        if name and image and pdf and allowed_file(image.filename) and allowed_file(pdf.filename):
+            user_folder = os.path.join(app.config['UPLOAD_FOLDER'], name)
+            os.makedirs(user_folder, exist_ok=True)
+
+            image_path = os.path.join(user_folder, '1. ' + secure_filename(image.filename))
+            image.save(image_path)
+
+            pdf_path = os.path.join(user_folder, '2. ' + secure_filename(pdf.filename))
+            pdf.save(pdf_path)
+
+            # TODO: Implement Gemini integration for text extraction
+            # extracted_text = extract_text_with_gemini(image_path)
+            extracted_text = "Gemini text extraction will be implemented here using the image at " + image_path
+
+            return render_template('result.html', name=name, extracted_text=extracted_text)
+        else:
+            return "Invalid file or missing information."
+
+    return render_template('upload.html')
+
+if __name__ == '__main__':
+    app.run(debug=True)
+```
+
+**Create `templates/upload.html`:**
+```html
+<h1>Upload Files</h1>
+<form method="POST" enctype="multipart/form-data">
+    <input type="text" name="name" placeholder="Your Name" required><br>
+    <input type="file" name="image" accept="image/*" required><br>
+    <input type="file" name="pdf" accept="application/pdf" required><br>
+    <input type="submit" value="Submit">
+</form>
+```
+
+**Create `templates/result.html`:**
+```html
+<h1>Results for {{ name }}</h1>
+<p>Extracted Text: {{ extracted_text }}</p>
+```
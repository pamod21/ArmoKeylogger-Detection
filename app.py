import gradio as gr
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the machine learning model and data preprocessing parameters
model = joblib.load('model.joblib')
means = joblib.load('m.joblib')
stds = joblib.load('s.joblib')

def predict_category(test_data):
  test = [float(x) for x in test_data.split()]
  for i in range(len(test)):
    test[i] = abs(test[i] - means[i]) / stds[i]
    test[i] = float(test[i])
  v = rfc1.predict([test])
  if(v == 1):
      return "keylogger is detected"
  return "keylogger is not detected"
  # return v

# input_text = [gr.inputs.Textbox(label='Input')]
input_text= gr.inputs.Textbox(label="Enter 15 inputs")
output_text = gr.outputs.Textbox(label='output')
interface = gr.Interface(fn=predict_category, inputs=input_text, outputs=output_text)

# Launch the interface
interface.launch()
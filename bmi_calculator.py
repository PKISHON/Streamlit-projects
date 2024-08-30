import streamlit as st

# Define custom CSS for styling
custom_css = """
<style>
body {
    background-color: #f0f2f6;
    font-family: Arial, sans-serif;
}
.container {
    max-width: 600px;
    margin: auto;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
h1 {
    color: #333;
    text-align: center;
}
input, select, button {
    border-radius: 4px;
    padding: 10px;
    border: 1px solid #ddd;
    margin: 10px 0;
}
input[type="number"] {
    width: 100%;
}
button {
    background-color: #007bff;
    color: white;
    border: none;
    cursor: pointer;
}
button:hover {
    background-color: #0056b3;
}
.result {
    margin-top: 20px;
    padding: 10px;
    border-radius: 4px;
}
.result.normal {
    background-color: #d4edda;
    color: #155724;
}
.result.overweight {
    background-color: #fff3cd;
    color: #856404;
}
.result.obesity {
    background-color: #f8d7da;
    color: #721c24;
}
</style>
"""

def calculate_bmi(weight, height):
    # Convert height from cm to meters
    height_m = height / 100
    # Calculate BMI
    bmi = weight / (height_m ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "normal"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "normal"
    elif 25 <= bmi < 29.9:
        return "Overweight", "overweight"
    else:
        return "Obesity", "obesity"

def main():
    st.markdown(custom_css, unsafe_allow_html=True)
    st.title("BMI Calculator")

    # Container for the form
    with st.container():
        st.markdown('<div class="container">', unsafe_allow_html=True)
        
        # Input fields
        weight = st.number_input("Weight (kg)", min_value=1.0, format="%.1f")
        height = st.number_input("Height (cm)", min_value=1.0, format="%.1f")

        # Calculate BMI button
        if st.button("Calculate BMI"):
            if weight > 0 and height > 0:
                bmi = calculate_bmi(weight, height)
                category, class_name = get_bmi_category(bmi)
                result_message = f"Your BMI is: {bmi:.1f} - {category}"
                st.markdown(f'<div class="result {class_name}">{result_message}</div>', unsafe_allow_html=True)
            else:
                st.error("Please enter valid values for weight and height.")

        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

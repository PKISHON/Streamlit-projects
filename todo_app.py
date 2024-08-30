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
}
button {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 10px 20px;
    cursor: pointer;
}
button:hover {
    background-color: #0056b3;
}
input[type="text"] {
    width: calc(100% - 120px);
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    margin-right: 10px;
}
ul {
    list-style: none;
    padding: 0;
}
li {
    background-color: #f9f9f9;
    margin: 10px 0;
    padding: 10px;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
li.completed {
    text-decoration: line-through;
    color: #999;
}
</style>
"""

def main():
    st.markdown(custom_css, unsafe_allow_html=True)
    st.title("To-Do List")

    # Initialize session state for tasks
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    # Input for new task
    with st.form(key="task_form"):
        task_input = st.text_input("Add a new task")
        submit_button = st.form_submit_button("Add Task")

        if submit_button and task_input:
            st.session_state.tasks.append({"task": task_input, "completed": False})
            st.session_state.task_input = ""  # Clear input field

    # Display the list of tasks
    if st.session_state.tasks:
        for index, task in enumerate(st.session_state.tasks):
            col1, col2 = st.columns([8, 2])
            with col1:
                task_class = "completed" if task["completed"] else ""
                st.markdown(f'<li class="{task_class}">{task["task"]}</li>', unsafe_allow_html=True)
            with col2:
                if st.button("Complete", key=f"complete_{index}"):
                    st.session_state.tasks[index]["completed"] = True
                    # Manually update the session state
                    st.session_state.tasks = st.session_state.tasks  # Triggers UI update

    # Button to clear completed tasks
    if st.button("Clear Completed Tasks"):
        st.session_state.tasks = [task for task in st.session_state.tasks if not task["completed"]]
        # Manually update the session state
        st.session_state.tasks = st.session_state.tasks  # Triggers UI update

if __name__ == "__main__":
    main()

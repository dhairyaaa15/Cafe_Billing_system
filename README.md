<h2>Project Description</h2>
<p>This project is a Cafe Billing System built using Python's <code>tkinter</code> library for the graphical user interface (GUI). The application is designed to manage and generate bills for a cafe, allowing users to select items from a menu, calculate the total cost, apply discounts, and save the bill details in a CSV file. Additionally, the system can generate a printable bill in a text file format.</p>

<p>The application includes various validation checks to ensure that the input data is accurate and meets the required criteria. It also provides a user-friendly interface with options to reset the form, calculate the total bill, and print the bill.</p>

<h2>Key Features</h2>
<h3>User Input Validation:</h3>
<ul>
    <li>Validates fields such as name and phone number.</li>
    <li>Ensures that mandatory fields are filled and that the input data is in the correct format.</li>
</ul>

<h3>Menu Selection:</h3>
<ul>
    <li>Allows users to select items from a menu, including burgers, garlic bread, tacos, pastas, fries, shakes, and cold coffee.</li>
    <li>Provides buttons to increase or decrease the quantity of each item.</li>
</ul>

<h3>Bill Calculation:</h3>
<ul>
    <li>Calculates the total cost of the selected items.</li>
    <li>Applies SGST and CGST taxes.</li>
    <li>Allows for the application of discounts.</li>
</ul>

<h3>Bill Display:</h3>
<ul>
    <li>Displays the bill in a text area within the application.</li>
    <li>Includes details such as customer name, phone number, date, time, bill number, itemized list of selected items, subtotal, taxes, discount, and grand total.</li>
</ul>

<h3>Data Storage:</h3>
<ul>
    <li>Saves the bill details in a CSV file (<code>cafe_details.csv</code>) for record-keeping.</li>
    <li>Generates a printable bill in a text file format.</li>
</ul>

<h3>User Interface:</h3>
<ul>
    <li>Provides a clean and intuitive GUI with options to navigate between different sections (Menu, Help, About).</li>
    <li>Includes a display area to show the generated bill and user details.</li>
</ul>

<h2>Installation</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/yourusername/cafe-billing-system.git</code></pre>
    </li>
    <li>Navigate to the project directory:
        <pre><code>cd cafe-billing-system</code></pre>
    </li>
    <li>Run the application:
        <pre><code>python main.py</code></pre>
    </li>
</ol>

<h2>Usage</h2>
<ol>
    <li>Launch the application.</li>
    <li>Fill in the required details in the form (Name, Contact Number).</li>
    <li>Select items from the menu and adjust quantities using the "+" and "-" buttons.</li>
    <li>Click on "Calculate" to generate the bill.</li>
    <li>Click on "Print" to save the bill details and generate a printable bill.</li>
    <li>Use the "RESET" button to clear the form and start over.</li>
</ol>

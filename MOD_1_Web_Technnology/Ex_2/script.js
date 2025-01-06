// DOM Elements
const expenseForm = document.getElementById('expense-form');
const expenseTable = document.getElementById('expense-table');
const expenseChartCtx = document.getElementById('expense-chart').getContext('2d');

// Initialize expenses array from localStorage
let expenses = JSON.parse(localStorage.getItem('expenses')) || [];

// Initialize Chart.js chart
let chart;
function updateChart() {
    const categories = expenses.reduce((acc, expense) => {
        acc[expense.category] = (acc[expense.category] || 0) + expense.amount;
        return acc;
    }, {});

    const labels = Object.keys(categories);
    const data = Object.values(categories);

    if (chart) chart.destroy(); // Destroy existing chart

    chart = new Chart(expenseChartCtx, {
        type: 'pie',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: ['#ff6384', '#36a2eb', '#ffcd56', '#4bc0c0']
            }]
        }
    });
}

// Render expenses table
function renderExpenses() {
    expenseTable.innerHTML = ''; // Clear table rows
    expenses.forEach((expense, index) => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${index + 1}</td>
            <td>$${expense.amount}</td>
            <td>${expense.description}</td>
            <td><span class="badge bg-secondary">${expense.category}</span></td>
            <td>
                <button class="btn btn-danger btn-sm" onclick="deleteExpense(${index})">Delete</button>
            </td>
        `;
        expenseTable.appendChild(row);
    });
    updateChart(); // Update chart after rendering
}

// Add expense
expenseForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const amount = parseFloat(document.getElementById('amount').value);
    const description = document.getElementById('description').value;
    const category = document.getElementById('category').value;

    if (amount && description && category) {
        expenses.push({ amount, description, category });
        localStorage.setItem('expenses', JSON.stringify(expenses));
        expenseForm.reset();
        renderExpenses();
    }
});

// Delete expense
function deleteExpense(index) {
    expenses.splice(index, 1);
    localStorage.setItem('expenses', JSON.stringify(expenses));
    renderExpenses();
}

// Initial render
renderExpenses();

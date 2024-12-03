// Theme Management
document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const icon = themeToggle.querySelector('i');
    
    // Vérifie si un thème est déjà stocké
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    updateThemeIcon(currentTheme);

    themeToggle.addEventListener('click', function() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme);
    });

    function updateThemeIcon(theme) {
        if (theme === 'dark') {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        }
    }
});

// Language Management
const languageItems = document.querySelectorAll('[data-language]');
const savedLanguage = localStorage.getItem('language') || 'fr';

languageItems.forEach(item => {
    item.addEventListener('click', function(e) {
        e.preventDefault();
        const language = this.getAttribute('data-language');
        localStorage.setItem('language', language);
        
        // Update active state
        languageItems.forEach(item => {
            item.classList.remove('active');
        });
        this.classList.add('active');
        
        // Update display text
        const dropdownButton = document.getElementById('languageDropdown');
        dropdownButton.innerHTML = `<i class="fas fa-globe me-1"></i> ${language.toUpperCase()}`;
        
        // Reload page with new language
        // window.location.href = `/${language}${window.location.pathname}`;
    });
    
    // Set initial active state
    if (item.getAttribute('data-language') === savedLanguage) {
        item.classList.add('active');
        const dropdownButton = document.getElementById('languageDropdown');
        dropdownButton.innerHTML = `<i class="fas fa-globe me-1"></i> ${savedLanguage.toUpperCase()}`;
    }
});

// Animations
document.addEventListener('DOMContentLoaded', function() {
    AOS.init({
        duration: 800,
        once: true,
        offset: 100
    });
});

// Charts (if present)
document.addEventListener('DOMContentLoaded', function() {
    const chartElements = document.querySelectorAll('[data-chart]');
    
    chartElements.forEach(element => {
        const chartType = element.getAttribute('data-chart');
        const ctx = element.getContext('2d');
        
        // Update chart colors based on theme
        function getChartColors(theme) {
            return theme === 'dark' ? {
                backgroundColor: [
                    'rgba(54, 162, 235, 0.8)',
                    'rgba(75, 192, 192, 0.8)',
                    'rgba(153, 102, 255, 0.8)',
                    'rgba(255, 159, 64, 0.8)'
                ],
                borderColor: '#343a40'
            } : {
                backgroundColor: [
                    'rgba(54, 162, 235, 0.8)',
                    'rgba(75, 192, 192, 0.8)',
                    'rgba(153, 102, 255, 0.8)',
                    'rgba(255, 159, 64, 0.8)'
                ],
                borderColor: '#ffffff'
            };
        }
        
        // Create and update charts
        let chart;
        function updateChart() {
            const theme = document.documentElement.getAttribute('data-theme');
            const colors = getChartColors(theme);
            
            if (chart) {
                chart.destroy();
            }
            
            const config = {
                type: chartType,
                data: {
                    // Chart data configuration
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom',
                            labels: {
                                color: theme === 'dark' ? '#f8f9fa' : '#212529'
                            }
                        }
                    }
                }
            };
            
            chart = new Chart(ctx, config);
        }
        
        // Initial chart creation
        updateChart();
        
        // Update chart on theme change
        document.documentElement.addEventListener('data-bs-theme-changed', updateChart);
    });
});

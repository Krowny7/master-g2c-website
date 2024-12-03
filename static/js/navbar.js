document.addEventListener('DOMContentLoaded', function() {
    let lastScrollTop = 0;
    const navbar = document.querySelector('.navbar');
    const scrollThreshold = 50; // Réduit le seuil pour une réaction plus rapide
    let isScrolling;

    // Ajouter la classe visible initialement
    navbar.classList.add('navbar-visible');

    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
        
        // Vérifier si nous avons dépassé le seuil de défilement
        if (currentScroll > scrollThreshold) {
            // Calculer la direction et la vitesse du défilement
            const scrollDelta = currentScroll - lastScrollTop;
            
            if (scrollDelta > 10) { // Défilement vers le bas significatif
                navbar.classList.remove('navbar-visible');
                navbar.classList.add('navbar-hidden');
            } else if (scrollDelta < -5) { // Défilement vers le haut léger
                navbar.classList.remove('navbar-hidden');
                navbar.classList.add('navbar-visible');
            }
        } else {
            // Au-dessus du seuil, toujours visible
            navbar.classList.remove('navbar-hidden');
            navbar.classList.add('navbar-visible');
        }

        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
    }, { passive: true });

    // Gérer le hover sur la navbar
    navbar.addEventListener('mouseenter', function() {
        navbar.classList.remove('navbar-hidden');
        navbar.classList.add('navbar-visible');
    });

    // Gérer le focus sur les éléments de la navbar
    navbar.addEventListener('focusin', function() {
        navbar.classList.remove('navbar-hidden');
        navbar.classList.add('navbar-visible');
    });
});

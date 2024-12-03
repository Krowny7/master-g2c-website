document.addEventListener("DOMContentLoaded", function() {
    // Lazy loading pour les images
    const lazyImages = document.querySelectorAll("img[data-src]");
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    }, {
        rootMargin: "50px 0px",
        threshold: 0.1
    });

    lazyImages.forEach(img => {
        // Créer un placeholder en attendant le chargement
        img.style.opacity = "0";
        img.style.transition = "opacity 0.3s ease-in";
        
        // Observer l'image
        imageObserver.observe(img);
        
        // Gérer le chargement
        img.onload = function() {
            img.style.opacity = "1";
        };
    });

    // Lazy loading pour les backgrounds
    const lazyBackgrounds = document.querySelectorAll("[data-background]");
    const backgroundObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const element = entry.target;
                element.style.backgroundImage = `url(${element.dataset.background})`;
                element.removeAttribute('data-background');
                observer.unobserve(element);
            }
        });
    }, {
        rootMargin: "50px 0px",
        threshold: 0.1
    });

    lazyBackgrounds.forEach(element => backgroundObserver.observe(element));
});

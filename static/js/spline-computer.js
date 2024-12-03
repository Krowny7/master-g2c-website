// Chargement du modèle Spline
async function loadSplineComputer() {
    const canvas = document.getElementById('spline-computer');
    if (!canvas) return;

    try {
        const spline = await import('https://unpkg.com/@splinetool/viewer@0.9.506/build/spline-viewer.js');
        const viewer = new spline.Application(canvas);
        await viewer.load('https://my.spline.design/cutecomputerfollowcursor-20ad4acfa36a2afa11bac72556123d5a/');
    } catch (error) {
        console.error('Erreur lors du chargement du modèle Spline:', error);
    }
}

// Initialisation au chargement de la page
document.addEventListener('DOMContentLoaded', loadSplineComputer);

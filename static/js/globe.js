import * as THREE from 'https://cdn.skypack.dev/three@0.132.2';

function createGlobe() {
    // Scene setup
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ 
        canvas: document.querySelector('#globe-canvas'),
        alpha: true,
        antialias: true 
    });

    // Set size
    const container = document.querySelector('#globe-container');
    const width = container.offsetWidth;
    const height = container.offsetHeight;
    renderer.setSize(width, height);

    // Create sphere
    const geometry = new THREE.SphereGeometry(5, 64, 64);
    const textureLoader = new THREE.TextureLoader();
    const texture = textureLoader.load('/static/img/earth-map.jpg');
    const material = new THREE.MeshPhongMaterial({
        map: texture,
        bumpMap: texture,
        bumpScale: 0.1,
    });
    const sphere = new THREE.Mesh(geometry, material);
    scene.add(sphere);

    // Add lights
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);
    const pointLight = new THREE.PointLight(0xffffff, 1);
    pointLight.position.set(15, 15, 15);
    scene.add(pointLight);

    // Position camera
    camera.position.z = 15;

    // Animation
    let rotationSpeed = 0.001;
    function animate() {
        requestAnimationFrame(animate);
        sphere.rotation.y += rotationSpeed;
        renderer.render(scene, camera);
    }

    // Handle window resize
    window.addEventListener('resize', () => {
        const width = container.offsetWidth;
        const height = container.offsetHeight;
        camera.aspect = width / height;
        camera.updateProjectionMatrix();
        renderer.setSize(width, height);
    });

    // Handle mouse interaction
    let isDragging = false;
    let previousMousePosition = {
        x: 0,
        y: 0
    };

    container.addEventListener('mousedown', (e) => {
        isDragging = true;
    });

    container.addEventListener('mousemove', (e) => {
        if (isDragging) {
            const deltaMove = {
                x: e.offsetX - previousMousePosition.x,
                y: e.offsetY - previousMousePosition.y
            };

            sphere.rotation.y += deltaMove.x * 0.005;
            sphere.rotation.x += deltaMove.y * 0.005;

            rotationSpeed = 0;
        }

        previousMousePosition = {
            x: e.offsetX,
            y: e.offsetY
        };
    });

    container.addEventListener('mouseup', () => {
        isDragging = false;
        rotationSpeed = 0.001;
    });

    // Start animation
    animate();
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', createGlobe);

var height = window.innerHeight;
var width = window.innerWidth;
var scene, camera, renderer;
var container;
var planeGeometry;
var planeMaterial;
var plane;
var main_light;
var point_light;
var skyboxGeometry;
var skyboxMaterial;
var skybox;





function init() {
    camera = new THREE.PerspectiveCamera(70, width, height, 1, 2000)
    camera.positon.set(0,-40,50);

    screne= new THREE.Scene();
    
    renderer = new THREE.WebGLRenderer();
    renderer = setPixelRatio(window.devicePixelRatio);
    renderer.setSize(width, height);

    planeGeometry = new THREE.PlaneGeometry(10,20,32);
    planeMaterial = new THREE.MeshBasicMaterial( {color: 0xffff00});
    plane = new THREE.Mesh(planeGeometry, planeMaterial);
    NavigationPreloadManager.positon.set(0,0,-1);
    scene.add(plane)

    main_light = new THREE.AmbientLight(0x404040);
    scene.add(main_light)

    skyboxGeometry = new THREE.CubeGeometry(10000,10000,10000);
    skyboxMaterial = new THREE.MeshBasicMaterial({color: 0xffff00, side:THREE.BackSide})
    skybox = new THREE.Mesh(skyboxGeometry, skyboxMaterial);
    scene.add(skybox)

    point_light = new THREE.PoingLight(0xffffff);
    point_light.positon.set(0,300,200);
    scene.add(pointLight);
}

function renderScene(){
    requestAnimationFrame(renderScene);
    renderScene.renderer(scene, camera)
}

init();
renderScene();
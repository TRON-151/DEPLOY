//Scene, Canvas, Renderer, light and Camera
const scene = new THREE.Scene();
const canvas = document.getElementById('threejsCanvas');
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ canvas });
//////////////////////////////
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);
/////////////////////////////
const light = new THREE.PointLight(0xffffff, 1);

// Positioning the main two things:
light.position.set(-10, -10, -5); scene.add(light);
camera.position.z = 5;

//First Sphere
const geometry_1 = new THREE.SphereGeometry(1, 32, 32);
const material_1 = new THREE.MeshStandardMaterial({ color: 0xff4500 });
const sphere_1 = new THREE.Mesh(geometry_1, material_1);

sphere_1.position.set(0, 0, 0);
scene.add(sphere_1);

//Second Sphere
const geometry_2 = new THREE.SphereGeometry(0.5, 32, 32);
const material_2 = new THREE.MeshStandardMaterial({ color: 0xff4500 });
const sphere_2 = new THREE.Mesh(geometry_2, material_2);

sphere_2.position.set(0, 0, 1);
// scene.add(sphere_2);

//Third Sphere
const geometry_3 = new THREE.SphereGeometry(1.7, 32, 32);
const material_3 = new THREE.MeshStandardMaterial({ color: 0xff4500 });
const sphere_3 = new THREE.Mesh(geometry_3, material_3);

sphere_3.position.set(0, 0, -1.5);
scene.add(sphere_3);


function animate() {
   requestAnimationFrame(animate);

   // sphere_1.rotation.x += 0.01;
   // sphere_1.rotation.y += 0.01;

   renderer.render(scene, camera);
}
animate();

// Resize Handler
window.addEventListener('resize', () => {
   camera.aspect = window.innerWidth / window.innerHeight;
   camera.updateProjectionMatrix();
   renderer.setSize(window.innerWidth, window.innerHeight);
});

/////////////////////Login Details///////////////////////////////////
function openPopup() {
   document.getElementById('popup').style.display = 'flex';
}

function closePopup() {
   document.getElementById('popup').style.display = 'none';
}

function showForm(formType) {
   document.getElementById('login-form').style.display = 'none';
   document.getElementById('signup-form').style.display = 'none';

   if (formType === 'login') {
      document.getElementById('login-form').style.display = 'block';
   } else if (formType === 'signup') {
      document.getElementById('signup-form').style.display = 'block';
   }
}

function login() {
   alert('Logging in with username: ' + document.getElementById('login-username').value);
   closePopup();
}

function signup() {
   alert('Signing up with username: ' + document.getElementById('signup-username').value);
   closePopup();
}

//////////////////////////Signup backend////////////////////////////////
async function signup() {
   const username = document.getElementById('signup-username').value;
   const email = document.getElementById('signup-email').value;
   const password = document.getElementById('signup-password').value;

   try {
      const response = await fetch('http://localhost:3000/signup', {
         method: 'POST',
         headers: {
            'Content-Type': 'application/json',
         },
         body: JSON.stringify({ username, email, password }),
      });

      const result = await response.json();
      alert(result.message);
   } catch (error) {
      console.error('Error:', error);
   }
}
//////////////////////////////////////////////////////////////////////

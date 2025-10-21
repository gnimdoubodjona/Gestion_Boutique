document.addEventListener("DOMContentLoaded", () => {
  const tl = gsap.timeline({ defaults: { ease: "power3.out", duration: 1 } });

  // 1️⃣ Texte de gauche (progressif)
  tl.fromTo(".hero-text .left p, .hero-text .left h1, .hero-text .left .desc2", 
    { opacity: 0, y: 50 }, 
    { opacity: 1, y: 0, stagger: 0.4 }
  );

  // 2️⃣ Bouton (après les textes)
  tl.fromTo(".hero-text .left button", 
    { opacity: 0, y: 30 }, 
    { opacity: 1, y: 0, duration: 1 }, 
    "+=0.3"
  );

  // 3️⃣ Texte de droite "Stylee / Killer"
  tl.fromTo(".hero-text .right p", 
    { opacity: 0, y: 60 }, 
    { opacity: 1, y: 0, stagger: 0.5, duration: 1.2 }, 
    "+=0.5"
  );
});

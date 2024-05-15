gsap.registerPlugin(ScrollTrigger);
document.getElementById("home").addEventListener("click", function () {
  window.location.href = "/";
});
const popupAnimation = (target) =>
  gsap.fromTo(
    target,
    {
      scale: 0,
    },
    {
      scale: 1,
      ease: "bounce.out",
      duration: 0.3,
      display: "block",
    }
  );

function toggleMenu() {
  var menu = document.getElementById("popup-menu");
  popupAnimation(menu).play();
}

document.addEventListener("click", function (event) {
  var target = event.target;
  var menu = document.getElementById("popup-menu");
  popupAnimation(menu).reversed(true);
});

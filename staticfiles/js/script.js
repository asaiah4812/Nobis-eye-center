let menubar = document.querySelector("#menu-bar");
let mynav = document.querySelector(".navbar");

menubar.onclick = () => {
  menubar.classList.toggle("fa-times");
  mynav.classList.toggle('active')
};


function toggleVideo(){
  const trailer = document.querySelector('.trailer')
  const video = document.querySelector('video');
  video.pause();
  trailer.classList.toggle('active')
}; 


// gallery slider

const initSlider = () => {
  const imageList = document.querySelector(".slider-wrapper .image-list");
  const slideButtons = document.querySelectorAll(".slide-wrapper .slide-button");

  slideButtons.forEach(button => {
    button.addEventListener("click", () =>{
      const direction = button.id === "prev-slide" ? -1 : 1;
      const scrollAmount = imageList.clientWidth * direction;
      imageList.scrollBy({ left: scrollAmount, behavior: "smooth"});
    })
  })
}

window.addEventListener("load", initSlider);
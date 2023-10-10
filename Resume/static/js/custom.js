var sections = document.querySelectorAll('.form-section')
let currentProgress = 0

function updateProgress() {
  const percent = ((currentProgress + 1) / sections.length) * 100
  document.getElementById("myBar").style.width = percent + "%";
}


function showSection(sectionIndex){
  sections.forEach((section, index) => {
    if (index === sectionIndex){
      section.style.display = "block"
    }
    else{
      section.style.display = "none";
    }
  })
  currentProgress = sectionIndex;

  updateProgress();
}

const nextBtns = document.querySelectorAll('.next-button')
const prevBtns = document.querySelectorAll('.prev-button')

nextBtns.forEach((btn, index) =>{
  btn.addEventListener('click', function(e){
    e.preventDefault();
    if(currentProgress < sections.length - 1){
      showSection(currentProgress + 1)
    }
  })
  showSection(0)
})


prevBtns.forEach((btn, index) =>{
  btn.addEventListener('click', function(e){
    e.preventDefault();
    if(currentProgress <= sections.length - 1){
      
      showSection(currentProgress - 1)
    }
  })
  showSection(0)
})




// *********************************
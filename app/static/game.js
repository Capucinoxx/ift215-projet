const CIRCLE_SIZE = 70; // 70px;

const colors = ["#FF6633", "#FFB399", "#FF33FF", "#FFFF99", "#00B3E6"];

(() => {
  const container = document.getElementById("game-container");
  if (!container) return;

  const counter = document.getElementById("counter");
  if (!counter) return;

  let count = 0;

  const generate_circle = (time) => {
    const circle = document.createElement("div");
    circle.classList.add("circle");

    const color = colors[Math.floor(Math.random() * colors.length)];
    circle.style.backgroundColor = color;

    circle.style.left = `${
      Math.random() * (window.innerWidth - CIRCLE_SIZE)
    }px`;
    circle.style.top = `${
      Math.random() * (window.innerHeight - CIRCLE_SIZE)
    }px`;

    circle.addEventListener("click", () => {
      circle.remove();
      count++;
      counter.innerHTML = count;
    });

    container.appendChild(circle);

    fade_out_animation(circle, time);
  };

  const fade_out_animation = (circle, time) => {
    let opacity = 1;

    const interval = setInterval(() => {
      if (opacity <= 0) {
        clearInterval(interval);
        circle.remove();
      } else {
        circle.style.opacity = opacity;
        opacity -= 0.05;
      }
    }, time);
  };

  let time = 0;
  setInterval(() => {
    const interval = Math.sin(time) * 500 + 300;
    time += 0.1;
    generate_circle(interval);
  }, 2500);
})();

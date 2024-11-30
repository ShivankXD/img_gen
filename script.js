document.getElementById("generate-btn").addEventListener("click", async () => {
    const prompt = document.getElementById("prompt").value;
    const genre = document.getElementById("genre").value;
  
    if (!prompt.trim()) {
      alert("Please enter a prompt!");
      return;
    }
  
    // Show loading spinner
    const loading = document.querySelector(".loading");
    loading.style.display = "block";
  
    // Hide previous image
    const img = document.getElementById("generated-image");
    img.style.display = "none";
  
    try {
      const response = await fetch("/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt, genre }),
      });
  
      if (!response.ok) {
        throw new Error("Image generation failed!");
      }
  
      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
  
      // Display the generated image
      img.src = url;
      img.style.display = "block";
      loading.style.display = "none";
    } catch (error) {
      alert(error.message);
      loading.style.display = "none";
    }
  });
  
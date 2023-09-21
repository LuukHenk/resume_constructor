const download_pdf_button = document.getElementById("download_button_id")
let loaded_scripts = []

function load_script(url) {
    if (loaded_scripts.includes(url)) {
        return Promise.resolve()
    } else {
        return new Promise(function(resolve, reject) {
            const script = document.createElement("script")
            script.setAttribute("src", url)
            script.addEventListener("load", resolve)
            script.addEventListener("error", reject)
            document.body.appendChild(script)
            loaded_scripts.push(url)
        })
    }
}

download_pdf_button.addEventListener("click", async function() {
    console.log("Loading elements of interest")
    elements_to_render = document.getElementById("html_body_id")

    console.log("Loading scripts")
    // https://ekoopmans.github.io/html2pdf.js/
    await load_script("https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js")

    console.log("Generating pdf")
    const options = {
        html2canvas: {dpi: 92},
        pagebreak: {mode: 'avoid-all'},
        filename: "Resume_Luuk_Perdaems.pdf",
    }
    html2pdf().set(options).from(elements_to_render).save()
    console.log("Done generating pdf")
})

export function handleIsWorking() {
    let checkboxes = document.querySelectorAll(".all-staff")
    for (let i = 0; i < checkboxes.length; i++) {
        checkboxes[i].addEventListener("change", (e) => {
            let row = e.target.closest("tr")

            // select when your break starts, add td then input inside that
            let breakStart = document.createElement("td")
            let timeInput = document.createElement("input")

            timeInput.type = "time"
            timeInput.required = true
            const count = i
            timeInput.name = "brStart" + count

            // select how long your break is, 45 or 60 min
            let breakLength = document.createElement("td")
            let lengthSelect = document.createElement("select")
            lengthSelect.name = "brLen" + count

            let shortBreak = document.createElement("option")
            shortBreak.value = 45
            shortBreak.text = "45 min"

            let longBreak = document.createElement("option")
            longBreak.value = 60
            longBreak.text = "60 min"

            lengthSelect.appendChild(shortBreak)
            lengthSelect.appendChild(longBreak)

            breakStart.appendChild(timeInput);
            breakLength.appendChild(lengthSelect)

            row.appendChild(breakStart)
            row.appendChild(breakLength)
        })
    }
}

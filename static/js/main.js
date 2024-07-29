import { handleIsWorking } from "./modules/staff.js";
import { makeTimeSlots, submitOpenTimeSlots } from "./modules/timeSlotUtils.js";

const N = 29
makeTimeSlots(N)
handleIsWorking()
window.submitOpenTimeSlots = () => {
    submitOpenTimeSlots(N)
}

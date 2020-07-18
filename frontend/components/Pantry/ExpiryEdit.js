import styles from "./Pantry.module.scss";

import Modal from "../modal/Modal";
import { useDispatch, useSelector } from "react-redux";
import { change_expiry, clear_expiry } from "../../lib/redux/actions/expiryAction";
import { change } from "../../lib/redux/actions/pantryAction";

export default function ExpiryEdit() {
    const dispatch = useDispatch();
    const curr = useSelector(state => state.expiry)

    function handleSubmit(event) {
        event.preventDefault();
        dispatch(change_expiry(event.target.elements.expiry.value))
        dispatch((change(curr.name, curr.category, event.target.elements.expiry.value)))
        event.target.elements.expiry.value = undefined
        document.getElementById("expiry-edit").classList.toggle("is-active")
    }
    console.log(curr.expiry)
    let content = ( <div>
            <h3 className="title is-3">Ingredient - {curr.name}</h3>
            <h4 className="title is-5">Category - {curr.category}</h4>
            { curr.expiry ? <h4 className="title is-5">Expiry date - {curr.expiry}</h4> : ""}
            <hr/>
            <form onSubmit={handleSubmit}>
                <div className="form">
                    <label className="label">Update Expiry Date</label>
                    <div className="field control">
                        <input required={true} name="expiry" className="input" type="date"/>
                    </div>
                    <div className="field is-grouped control">
                    <div className="control">
                            <button type="submit" className="button is-link">
                                Update
                            </button>
                        </div>
                        <div className="control">
                            <button onClick={(e) => {e.preventDefault(); document.getElementById("expiry-edit").classList.toggle("is-active")}} type="submit" className="button">
                                Cancel
                            </button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    )
    return <Modal id="expiry-edit" content={content} func={clear_expiry}/>
}
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
    }

    let content = (
        <form onSubmit={handleSubmit}>
            <div className="form">
                <h3 className="title is-3">Update Ingredient</h3>
                <hr/>
                <label className="label">Expiry Date</label>
                <div className="field control">
                    <input required={true} name="expiry" className="input" type="date"/>
                </div>
                <hr/>
                <div className="field control">
                    <button type="submit" className="button is-link">
                        Save
                    </button>
                </div>
            </div>
        </form>
    )
    return <Modal id="expiry-edit" content={content} func={clear_expiry}/>
}
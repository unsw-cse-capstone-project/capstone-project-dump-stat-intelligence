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
        toggleForm();
    }
    
    function toggleForm() {
        let form = document.getElementById("expiry-form");
        if (form.style.maxHeight) {
            form.style.maxHeight = form.scrollHeight + 'px';
            setTimeout(() => form.style.maxHeight = null, 5);
        } else {
            form.style.maxHeight = form.scrollHeight + 'px';
            setTimeout(() => form.style.maxHeight = 'none', 305);
        }
    }
    
    
    
    let content = <div>
            <h3 className="title is-3">Ingredient - {curr.name}</h3>
            <h4 className="title is-5">Category - {curr.category}</h4>
            <p>
                <span className="title is-5">Expiry date - {curr.expiry ? curr.expiry : <i>Not set</i>}</span>
                &nbsp;&nbsp;&nbsp;<a onClick={toggleForm} className={`is-link`}>Update expiry</a>
            </p>
            <hr/>
            <form id="expiry-form" className={styles.expiryForm} onSubmit={handleSubmit}>
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
                            <button onClick={(e) => {e.preventDefault(); toggleForm()}} type="submit" className="button">
                                Cancel
                            </button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    return <Modal id="expiry-edit" content={content} func={clear_expiry}/>
}
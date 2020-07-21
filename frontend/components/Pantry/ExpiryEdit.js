import styles from "./Pantry.module.scss";

import Modal from "../modal/Modal";
import { useDispatch, useSelector } from "react-redux";
import { change_expiry, clear_expiry } from "../../lib/redux/actions/expiryAction";
import { change } from "../../lib/redux/actions/pantryAction";
import { remove } from "../../lib/redux/actions/pantryAction";


export default function ExpiryEdit() {
    const dispatch = useDispatch();
    const curr = useSelector(state => state.expiry)

    function handleSubmit(event) {
        event.preventDefault();
        dispatch(change_expiry(event.target.elements.expiry.value))
        dispatch((change(curr.name, curr.category, event.target.elements.expiry.value)))
        event.target.elements.expiry.value = null
        toggleForm();
    }

    function handleDelete(event) {
        dispatch(remove({ingredient : curr.name, category : curr.category}));
        dispatch(clear_expiry());
        document.getElementById("expiry-edit").classList.toggle("is-active");
    }
    
    function toggleForm() {
        let form = document.getElementById("expiry-form");
        if (form.style.maxHeight) {
            form.style.maxHeight = form.scrollHeight + 'px';
            setTimeout(() => form.style.maxHeight = null, 5);
        } else {
            form.style.maxHeight = form.scrollHeight + 'px';
            setTimeout(() => form.style.maxHeight = 'none', 405);
        }
    }
    
    let alert = null;
    let days = null;
    if (curr.expiry) {
        days = (new Date(curr.expiry) - new Date()) / (1000 * 60 * 60 * 24);
        if (days < 0) {
            alert = "This ingredient has expired :("
        } else if (days < 7) {
            alert = "This ingredient is about to expire"
        } 
    }
    
    let content = <div>
            <h3 className="title is-3">Ingredient - {curr.name}</h3>
            {
                alert ? <div className={`notification is-light ${days < 0 ? "is-danger" : "is-danger"} ${styles.expiryAlert}`}>
                    {alert}
                </div> 
                : ""
            }
            <h4 className="title is-5">Category - {curr.category}</h4>
            <p>
                <span className="title is-5">Expiry date - {curr.expiry ? curr.expiry : <i>Not set</i>}</span>
                &nbsp;&nbsp;&nbsp;<a onClick={toggleForm} className={`is-link`}>Update expiry</a>
            </p>
            
            <form id="expiry-form" className={styles.expiryForm} onSubmit={handleSubmit}>
                <div style={{width:"100%"}} className="form">
                    <hr/>
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
                    <hr/>
                </div>
            </form>
            <div className={styles.expiryDelete}>
                <button onClick={handleDelete} className={`button is-primary ${styles.deleteButton}`}>
                    Delete ingredient
                </button>
            </div>
        </div>
    return <Modal id="expiry-edit" content={content} func={clear_expiry}/>
}
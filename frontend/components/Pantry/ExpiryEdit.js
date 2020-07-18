import styles from "./Pantry.module.scss";

import Modal from "../modal/Modal";

export default function ExpiryEdit() {


    let content = (
        <form>
            <div className="form">
                <h3 className="title is-3">Update Ingredient</h3>
                <hr/>
                <label className="label">Expiry Date</label>
                <div className="field control">
                    <input required={true} name="expiry" className="input" type="date"/>
                </div>
                <div className="field control">
                    <button type="submit" className="button is-link">
                        Save
                    </button>
                </div>
            </div>
        </form>
    )
    return <Modal id="expiry-edit" content={content} func={null}/>
}
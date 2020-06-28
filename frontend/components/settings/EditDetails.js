import style from "./EditDetails.module.scss";

import Modal from "../modal/Modal";

export default function EditDetails(props) {
    let form = <form>
        <div className="form">
            <h3 className="title is-3">Update details</h3>
            <hr/>
            <label className="label">Name</label>
            <div className="field-body field control">
                <div className="field control">
                    <input class="input" type="text" placeholder="First Name"/>
                </div>
                <div className="field control">
                    <input class="input" type="text" placeholder="Last Name"/>
                </div>
            </div>
            <label className="label">Phone Number</label>
            <div className="field control">
                <input className="input" type="tel" placeholder="Your Phone Number"></input>
            </div>
            <label className="label">Address</label>
            <div className="field control">
                <input className="input" type="text" placeholder="Your Address"></input>
            </div>
            <hr/>
            <div className="field control">
                <button class="button is-link">Update</button>
            </div>
        </div>
    </form>
    return <Modal id={props.id} content={form}/>
}
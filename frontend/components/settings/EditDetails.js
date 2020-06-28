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
                    <input class="input" type="text" placeholder="First Name" value={props.deets.first}/>
                </div>
                <div className="field control">
                    <input class="input" type="text" placeholder="Last Name" value={props.deets.last}/>
                </div>
            </div>
            <label className="label">Email</label>
            <div className="field control">
                <input className="input" type="text" placeholder="Your Address" value={props.deets.email}></input>
            </div>
            <label className="label">Phone Number</label>
            <div className="field control">
                <input className="input" type="tel" placeholder="Your Phone Number" value={props.deets.phone}></input>
            </div>
            <hr/>
            <div className="field control">
                <button class="button is-link">Update</button>
            </div>
        </div>
    </form>
    return <Modal id={props.id} content={form}/>
}
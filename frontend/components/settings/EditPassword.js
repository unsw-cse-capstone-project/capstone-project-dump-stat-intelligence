import Modal from "../modal/Modal"



export default function(props) {
    let form = <form>
        <h3 className="title is-3">Change password</h3>
        <hr/>
        <label className="label">Old password</label>
        <div className="field control">
            <input className="input" type="password" placeholder="..."></input>
        </div>
        <label className="label">New password</label>
        <div className="field control">
            <input className="input" type="password" placeholder="..."></input>
        </div>
        <hr/>
        <div className="field control">
            <button class="button is-link">Update</button>
        </div>
    </form>
    return <Modal id={props.id} content={form}/>
}
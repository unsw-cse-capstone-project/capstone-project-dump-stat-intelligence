import styles from "./Edit.module.scss";

import Modal from "../modal/Modal";

export default function NewIngredient(props) {
    const newIn = (e) => {
        e.preventDefault();
        console.log(e.target.elements.category.value, e.target.elements.name.value)
    }
    let content = <form onSubmit={newIn}>
        <h3 className="title is-3">Add ingredient to database</h3>
        <label className="label">Ingredient Name</label>
        <div className="field control">
            <input required={true} name="name" className="input" type="text" placeholder="name"/>
        </div>
        <label className="label">Category</label>
        <div className="field control">
            <div style={{width:"100%"}} className="select">
                <select name="category" style={{width:"100%"}}>
                    <option>VEG</option>
                </select>
            </div>
        </div>
        <div className="field control">
            <button type="submit" className="button is-primary">Commit Ingredient</button>
        </div>

    </form>
    return <Modal id={props.id} content={content}/>
}
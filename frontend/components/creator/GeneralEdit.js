import styles from "./Edit.module.scss";

import { useSelector, useDispatch } from 'react-redux';
import { update_create } from "../../lib/redux/actions/createAction";

export default function GeneralEdit() {
    const dispatch = useDispatch();
    let recipe = useSelector(state => state.create)
    function handleInput(event) {
        dispatch(update_create(event.target.name, event.target.value));
    }
    
    return <div className="form">
        <div className="field control">
            <label className="label">Title</label>
            <input
                name="name"
                className="input"
                type="text"
                value={recipe.name}
                onChange={handleInput}
            />
        </div>
        <div className="field control">
            <label className="label">Cook time</label>
            <input
                name="cook_time"
                className="input"
                type="text"
                value={recipe.cook_time}
                onChange={handleInput}
            />
        </div>
    </div>


}
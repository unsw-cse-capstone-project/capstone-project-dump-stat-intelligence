import styles from "./Edit.module.scss";

import { useSelector, useDispatch } from 'react-redux';
import { update_create } from "../../lib/redux/actions/createAction";

export default function MethodEdit() {
    const dispatch = useDispatch();
    let recipe = useSelector(state => state.create)
    function handleInput(event) {
        dispatch(update_create(event.target.name, event.target.value));
    }
    return <div className="field control">
        <label className="label">Method</label>
        <textarea
        className="textarea input"
        onChange={handleInput}
        name="method"
        value={recipe.method}
        ></textarea>
    </div>
}
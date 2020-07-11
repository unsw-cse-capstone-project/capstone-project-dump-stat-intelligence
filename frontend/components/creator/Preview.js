import styles from "./Edit.module.scss";


import { useSelector, useDispatch } from 'react-redux';
import { clear_create } from "../../lib/redux/actions/createAction";
import { useRouter } from 'next/router'


export default function Preview() {
    const dispatch = useDispatch();
    const router = useRouter();
    let creation = useSelector(state => state.create)
    
    function discard() {
        dispatch(clear_create());
        router.push("/cookbook")
    }

    return <div className="container">
        <div className="columns is-centred">
            <div className="box column is-10">
                <h1 className="title">Recipe Overview</h1>

                <div className="buttons">
                    {
                        creation.id ? <>
                            <button className="button is-light is-success">Add Recipe</button>
                            <button onClick={discard} className="button is-light is-danger">Discard</button>
                        </> : <>
                            <button className="button is-light is-success">Save Changes</button>
                            <button onClick={discard} className="button is-light is-danger">Discard Changes</button>
                        </>
                    }
                    
                </div>
            </div>
        </div>
    </div>


}
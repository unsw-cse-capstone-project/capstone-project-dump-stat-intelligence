import styles from "./Filter.module.scss";
import { useSelector } from "react-redux";
import Ingredient from "./Ingredient";

export default function FilterSearch(props) {
    let results = useSelector(state => state.search.results);

    return <>
            <div id={props.id} className={styles.searchHover}>
                {results.map((ingredient, idx) => (
                    <Ingredient runningList={true} searcher={props.searcher} key={idx} idx={idx} name={ingredient.name} expiry={ingredient.expiry} category={ingredient.category}/>
                ))}
            </div>

    </>

}
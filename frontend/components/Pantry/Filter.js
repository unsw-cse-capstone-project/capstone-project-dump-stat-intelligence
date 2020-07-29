import styles from "./Filter.module.scss";
import FilterItem from "./FilterItem";
import { recipes_update, recipes_unsuggest } from "../../lib/redux/actions/recipesAction";
import { useSelector, useDispatch } from "react-redux";
import { update_search, search_type } from "../../lib/redux/actions/searchAction";
import { explore_add, explore_clear, filter_update, filter_clear } from "../../lib/redux/actions/exploreAction";
import FilterSearch from "./FilterSearch";
import FilterIngredient from "./FilterIngredient";
import Check from "./Check";

export default function Filter() {
  const dispatch = useDispatch();
  let filters = useSelector((state) => state.explore.filters);
  let selections = useSelector(state => state.explore.ingredients);
  let pantryOnly = useSelector(state => state.search.pantryOnly);
  let suggestion = useSelector(state => state.recipes.suggestion);
  return (
    <div className={`form ${styles.filter}`} autoComplete="off">
      <div className="field is-grouped">
        <div className={`control ${styles.searchFormBox}`} onFocus={() => document.getElementById("explore-ing-add").classList.toggle(styles.show)} onBlur={() => setTimeout(() => document.getElementById("explore-ing-add").classList.remove(styles.show), 200)}>
          <FilterSearch id={"explore-ing-add"} searcher="explore-search"/>
          <input autocomplete="off" id="explore-search" placeholder="Search an ingredient" className="input" name="search" onChange={(e => {e.preventDefault(); dispatch(update_search(e.target.value))})}/>
          
        </div>
        <div className="control">
          <div onFocus={e => {let obj = document.getElementById("dropdown-menu4"); obj.classList.add(styles.show); obj.firstElementChild.focus();}} className={`select dropdown`}>
            <div className="dropdown-trigger">
              <button
                className="button"
                aria-haspopup="true"
                aria-controls="dropdown-menu4"
              >
                <span>Search from</span>
                <span className="icon is-small">
                  <i className="fas fa-check" aria-hidden="true"></i>
                </span>
              </button>
            </div>
            <div className={`dropdown-menu`} id="dropdown-menu4" role="menu">
              <div tabIndex="0" onBlur={e => {document.getElementById("dropdown-menu4").classList.remove(styles.show)}} className={`dropdown-content ${styles.stopBorder}`}>
                <a onClick={() => (dispatch(search_type(true)))} className="dropdown-item">
                  <span>Pantry ingredients only</span>
                  { pantryOnly ? <Check/> : ""}
                </a>
                <a onClick={() => (dispatch(search_type(false)))} className="dropdown-item">
                  <span>All ingredients</span>
                  { !pantryOnly ? <Check/> : ""}
                </a>
              </div>
            </div>
          </div>
        </div>
        
      </div>
      
      
      
      <div className="field is-grouped">
        <div className="control">
          <div onFocus={e => {let obj = document.getElementById("dropdown-menu5"); obj.classList.add(styles.show); obj.firstElementChild.focus();}} className="select dropdown">
            <div className="dropdown-trigger">
              <button
                className="button"
                aria-haspopup="true"
                aria-controls="dropdown-menu5"
              >
                <span>Meal type</span>
                <span className="icon is-small">
                  <i className="fas fa-check" aria-hidden="true"></i>
                </span>
              </button>
            </div>
            <div className="dropdown-menu" id="dropdown-menu5" role="menu">
              <div tabIndex="0" onBlur={e => {document.getElementById("dropdown-menu5").classList.remove(styles.show)}} className={`dropdown-content ${styles.stopBorder}`}>
                {Object.keys(filters.meal).map((key, idx) => (
                  <FilterItem
                    key={idx}
                    idx={idx}
                    category="meal"
                    name={key}
                    is_checked={filters.meal[key]}
                  />
                ))}
              </div>
            </div>
          </div>
        </div>
        <div className="control">
          <div onFocus={e => {let obj = document.getElementById("dropdown-menu6"); obj.classList.add(styles.show); obj.firstElementChild.focus();}} className="select dropdown">
            <div className="dropdown-trigger">
              <button
                className="button"
                aria-haspopup="true"
                aria-controls="dropdown-menu6"
              >
                <span>Dietary requirements</span>
                <span className="icon is-small">
                  <i className="fas fa-check" aria-hidden="true"></i>
                </span>
              </button>
            </div>
            <div className="dropdown-menu" id="dropdown-menu6" role="menu">
              <div tabIndex="0" onBlur={e => {document.getElementById("dropdown-menu6").classList.remove(styles.show)}} className={`dropdown-content ${styles.stopBorder}`}>
                {Object.keys(filters.diet).map((key, idx) => (
                  <FilterItem
                    key={idx}
                    category="diet"
                    name={key}
                    is_checked={filters.diet[key]}
                  />
                ))}
              </div>
            </div>
          </div>
        </div>
        <div className="control">
          <button onClick={e => {e.preventDefault(); dispatch(explore_clear()); dispatch(filter_clear())}} className="button">Reset search</button>
        </div>
        <div className="control">
          <button
            onClick={(event) => {
              event.preventDefault();
              dispatch(recipes_update());
            }}
            className="button is-primary"
          >
            <span>Search</span>
          </button>
        </div>
      </div>
      { suggestion ?
        <div className={styles.suggestBox}>
            <button onClick={e=> {e.stopPropagation(); dispatch(recipes_unsuggest())}} className="delete is_small"></button>
            <h6 className="is-6">&nbsp;Suggested ingredient -&nbsp;</h6>
            <span onClick={() => {dispatch(explore_add(suggestion)); dispatch(recipes_unsuggest());}} className={`tag is-primary ${styles.suggestion}`}>
              {suggestion}
            </span>
        </div>
        : ""
      }
      <div className={`tags ${styles.tags}`}>
        {
          selections.map((val, idx) => (
            <FilterIngredient ingredient={val} key={idx}/>

          ))
        }
      </div>
      <div className={`tags ${styles.tags}`}>
          {Object.keys(filters.meal).map((key, idx) => (
            filters.meal[key] ?  
            <span key={idx} className="tag is-dark">
                {key}
                <button onClick={() => dispatch(filter_update("meal", key, false))} className="delete is_small"></button>
            </span>
            : ""
          ))}
          {Object.keys(filters.diet).map((key, idx) => (
            filters.diet[key] ?  
            <span key={idx} className={`tag is-dark`}>
                {key}
                <button onClick={() => dispatch(filter_update("diet", key, false))} className="delete is_small"></button>
            </span>
            : ""
          ))}
      </div>
      
    </div>
  );
}

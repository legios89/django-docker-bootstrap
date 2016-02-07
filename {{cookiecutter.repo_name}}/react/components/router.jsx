/* global gettext */
var React = require('react');
var ReactDOM = require('react-dom');
var ReactRouter = require('react-router');
var Router = ReactRouter.Router;
var Route = ReactRouter.Route;
var createHashHistory = require('history/lib/createHashHistory');


var App = React.createClass({
  propTypes: {
    children: React.PropTypes.any
  },

  render: function () {
    return (
      <div className="site-wrapper-inner">
        <div className="cover-container">
          <div className="masthead clearfix">
            <div className="inner">
              <h3 className="masthead-brand">{gettext('Home')}</h3>
              <nav>
                <ul className="nav masthead-nav">
                  <li className="active"><a href="">{gettext('Home')}</a></li>
                  <li>
                    <a href="/admin/">{gettext('Admin')}</a>
                  </li>
                </ul>
              </nav>
            </div>
          </div>
          <div className="inner cover">
            {this.props.children}
          </div>
        </div>
      </div>);
  }
});

var NotFoundRoute = React.createClass({
  render: function () {
    return (<div>{gettext('NOT FOUND')}</div>);
  }
});

var Home = React.createClass({
  render: function () {
    return (
      <div>
        <h1 className="cover-heading">{gettext('It worked!')}</h1>
        <p className="lead">
          {gettext('Congratulations on your first Django-powered page.')}'
        </p>
      </div>
    );
  }
});

var history = createHashHistory({
  queryKey: false
});

ReactDOM.render((
  <Router history={history}>
    <Route component={App}>
      <Route path="/" component={Home}/>
      <Route path="*" component={NotFoundRoute}/>
    </Route>
  </Router>), document.getElementById('app-place'));

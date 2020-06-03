package nginx

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class NginxSimulation extends Simulation {

  val httpProtocol = http
    .baseUrl("http://nginx-ingress-controller.kube-system.svc")
    .header("Host", "loadtest.local")
    .acceptHeader("text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    .doNotTrackHeader("1")
    .acceptLanguageHeader("en-US,en;q=0.5")
    .acceptEncodingHeader("gzip, deflate")
    .userAgentHeader("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20100101 Firefox/16.0")

  val scn = scenario("Nginx basic test")
    .repeat(100, "n") {
      exec(
        http("request_1")
          .get("/")
      )
    }

  setUp(
    scn.inject(
      atOnceUsers(500),
      rampUsers(1500) during (15 seconds)
    ).protocols(httpProtocol))
    .maxDuration(5 minutes)
}

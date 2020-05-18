from typing import Tuple


class GatlingParser:
    def __init__(self, lines: str):
        split_lines = lines.splitlines()
        start_line_query = [i for i in range(
            len(split_lines)) if split_lines[i] == "Generating reports..."]
        assert len(start_line_query) == 1
        start_line = start_line_query[0]
        report_lines = split_lines[start_line + 2:start_line + 20]
        assert report_lines[0] == "================================================================================"
        assert report_lines[1] == "---- Global Information --------------------------------------------------------"

        total, ok, bad = self.parse_result_line(
            report_lines[2], "request count")
        self.request_count_total, self.request_count_ok, self.request_count_bad = int(
            total), int(ok), int(bad)
        self.request_success_ratio = float(
            self.request_count_ok) / float(self.request_count_total)
        self.request_failure = float(
            self.request_count_bad) / float(self.request_count_total)

        min_time, _, _ = self.parse_result_line(
            report_lines[3], "min response time")
        self.min_response_time = int(min_time)

        max_time, _, _ = self.parse_result_line(
            report_lines[4], "max response time")
        self.max_response_time = int(max_time)

        mean_time, _, _ = self.parse_result_line(
            report_lines[5], "mean response time")
        self.mean_response_time = int(mean_time)

        std_deviation, _, _ = self.parse_result_line(
            report_lines[6], "std deviation")
        self.std_deviation = int(std_deviation)

        response_time_50th_percentile, _, _ = self.parse_result_line(
            report_lines[7], "response time 50th percentile")
        self.response_time_50th_percentile = int(response_time_50th_percentile)

        response_time_75th_percentile, _, _ = self.parse_result_line(
            report_lines[8], "response time 75th percentile")
        self.response_time_75th_percentile = int(response_time_75th_percentile)

        response_time_95th_percentile, _, _ = self.parse_result_line(
            report_lines[9], "response time 95th percentile")
        self.response_time_95th_percentile = int(response_time_95th_percentile)

        response_time_99th_percentile, _, _ = self.parse_result_line(
            report_lines[10], "response time 99th percentile")
        self.response_time_99th_percentile = int(response_time_99th_percentile)

        mean_rps, _, _ = self.parse_result_line(
            report_lines[11], "mean requests/sec")
        self.mean_rps = int(mean_rps)

        assert report_lines[12] == "---- Response Time Distribution ------------------------------------------------"
        self.response_time_distribution = {}

        line = report_lines[13][2:]
        fields = list(filter(None, line.split(" ")))
        assert fields[0] == "t"
        upper = int(fields[2])
        self.response_time_distribution[(0, upper)] = int(fields[4])

        line = report_lines[14][2:]
        fields = list(filter(None, line.split(" ")))
        assert fields[3] == "t"
        lower = int(fields[0])
        upper = int(fields[5])
        self.response_time_distribution[(lower, upper)] = int(fields[7])

        line = report_lines[15][2:]
        fields = list(filter(None, line.split(" ")))
        assert fields[0] == "t"
        lower = int(fields[2])
        self.response_time_distribution[(lower, None)] = int(fields[4])

        line = report_lines[16][2:]
        fields = list(filter(None, line.split(" ")))
        assert fields[0] == "failed"

        assert report_lines[17] == "================================================================================"

    def parse_result_line(self, line, header: str) -> Tuple[str, str, str]:
        assert line[0:2] == "> "
        line = line[2:]
        assert line.find(header) >= 0
        fields = line[len(header):].split(" ")
        fields = list(filter(None, fields))
        total = fields[0]
        ok = fields[1].split("=")[1]
        bad = fields[2].split("=")[1]
        return total, ok, bad
